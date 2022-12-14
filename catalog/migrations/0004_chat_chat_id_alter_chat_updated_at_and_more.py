# Generated by Django 4.1 on 2022-08-15 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_hr_first_name_hr_is_bot_hr_last_name_hr_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='chat_id',
            field=models.CharField(max_length=20, null=True, verbose_name='Chat_ID'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 15, 10, 11, 36, 923258, tzinfo=datetime.timezone.utc), verbose_name='Когда обновлялся'),
        ),
        migrations.AlterField(
            model_name='hr',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 15, 10, 11, 36, 923866, tzinfo=datetime.timezone.utc), verbose_name='Дата обновления'),
        ),
    ]
