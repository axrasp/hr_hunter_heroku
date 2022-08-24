import json
import os

# для корректного переноса времени сообщений в json
from datetime import datetime

import django
from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from dotenv import load_dotenv
from telethon.sync import TelegramClient

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest, GetFullChannelRequest

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import ChannelParticipantsSearch

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

# импорт моделей
from catalog.models import HR, Chat

# Присваиваем значения внутренним переменным
load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
username = os.getenv('USERNAME')

client = TelegramClient(username, api_id, api_hash)

client.start()


@sync_to_async
def update_db_channel(channel):
    try:
        channel_request = Chat.objects.get(chat_id=channel.full_chat.id)
        print(f'Обновляю запись в БД Чатов {channel.chats[1].title}')
        channel.title = channel.chats[1].title
    except ObjectDoesNotExist:
        print('Чат не найден в БД')
        print(f'Cоздаю запись в БД Чатов {channel.chats[1].title}')
        channel_request = Chat.objects.create(
            chat_id=channel.full_chat.id,
            title=channel.chats[1].title
        )
    channel_request.save()
    return channel_request


@sync_to_async
def update_db_hr(participant, channel_db):
    try:
        hr = HR.objects.get(tg_id=participant.id)
        print(f'Обновляю запись в БД {participant.id}')
        hr.first_name = participant.first_name,
        hr.last_name = participant.last_name,
        hr.username = participant.username,
        hr.phone = participant.phone,
        hr.is_bot = participant.bot
        hr.chat.add(channel_db)
    except ObjectDoesNotExist:
        print('Запись не найдена')
        print(f'Cоздаю запись в БД {participant.id}')
        hr = HR.objects.create(
            tg_id=participant.id,
            first_name=participant.first_name,
            last_name=participant.last_name,
            username=participant.username,
            phone=participant.phone,
            is_bot=participant.bot
        )
        hr.chat.add(channel_db)
    hr.save()


async def get_all_participants(channel):
    """Получаем данные участников канала/чата"""
    offset_user = 0  # номер участника, с которого начинается считывание
    limit_user = 100  # максимальное число записей, передаваемых за один раз

    all_participants = []  # список всех участников канала
    filter_user = ChannelParticipantsSearch('')

    while True:
        channel_desc = await client(GetFullChannelRequest(channel)) # полные данные чата
        participants = await client(GetParticipantsRequest(
            channel,
            filter_user,
            offset_user,
            limit_user, hash=0
        ))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset_user += len(participants.users)

    all_users_details = []  # список словарей с интересующими параметрами участников канала

    channel_db = await update_db_channel(channel_desc)

    for participant in all_participants:
        await update_db_hr(participant, channel_db)  # обновление базы в БД
        """Собираем всех участников для JSON-файла"""
        all_users_details.append({"id": participant.id,
                                  "first_name": participant.first_name,
                                  "last_name": participant.last_name,
                                  "user": participant.username,
                                  "phone": participant.phone,
                                  "is_bot": participant.bot})

    with open('channel_users.json', 'w', encoding='utf8') as outfile:  # сохраянем JSON
        json.dump(all_users_details, outfile, ensure_ascii=False)


async def dump_all_messages(channel):
    """Записывает json-файл с информацией о всех сообщениях канала/чата"""
    offset_msg = 0  # номер записи, с которой начинается считывание
    limit_msg = 100  # максимальное число записей, передаваемых за один раз

    all_messages = []  # список всех сообщений
    total_messages = 0
    total_count_limit = 50  # поменяйте это значение, если вам нужны не все сообщения

    class DateTimeEncoder(json.JSONEncoder):
        '''Класс для сериализации записи дат в JSON'''

        def default(self, o):
            if isinstance(o, datetime):
                return o.isoformat()
            if isinstance(o, bytes):
                return list(o)
            return json.JSONEncoder.default(self, o)

    while True:
        history = await client(GetHistoryRequest(
            peer=channel,
            offset_id=offset_msg,
            offset_date=None, add_offset=0,
            limit=limit_msg, max_id=0, min_id=0,
            hash=0))
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            all_messages.append(message.to_dict())
        offset_msg = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break

    with open('channel_messages.json', 'w', encoding='utf8') as outfile:
        json.dump(
            all_messages,
            outfile,
            ensure_ascii=False,
            cls=DateTimeEncoder
        )


async def main():
    url = input("Введите ссылку на канал или чат: ")
    channel = await client.get_entity(url)
    await get_all_participants(channel)
    await dump_all_messages(channel)


with client:
    client.loop.run_until_complete(main())
