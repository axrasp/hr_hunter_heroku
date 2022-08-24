from django.db import models
from django.utils import timezone


class Chat(models.Model):
    chat_id = models.CharField(
        'Chat_ID',
        max_length=20,
        null=True
    )
    title = models.CharField(
        'title',
        max_length=20,
        null=True
    )
    created_at = models.DateTimeField(
        'Когда парсился чат',
        default=timezone.now,
        db_index=True
    )
    updated_at = models.DateTimeField(
        'Когда обновлялся',
        default=timezone.now(),
    )

    def __str__(self):
        return str(self.title)


class HR(models.Model):
    tg_id = models.CharField(
        'Tg ID',
        max_length=20,
        null=True
    )
    first_name = models.CharField(
        'First name',
        max_length=30,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        'Last name',
        max_length=30,
        blank=True,
        null=True
    )
    username = models.CharField(
        'Username',
        max_length=30,
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Phone',
        max_length=20,
        blank=True,
        null=True
    )
    is_bot = models.BooleanField(
        'Bot',
        blank=True,
        null = True
    )
    created_at = models.DateTimeField(
        'Когда парсился в первый раз',
        default=timezone.now,
        db_index=True
    )
    updated_at = models.DateTimeField(
        'Дата обновления',
        default=timezone.now(),
    )
    chat = models.ManyToManyField(
        Chat,
        verbose_name='В каких чатах состоит',
        related_name='hrs',
        blank=True
    )

    def __str__(self):
        return f"{str(self.tg_id)} - {self.username}"
