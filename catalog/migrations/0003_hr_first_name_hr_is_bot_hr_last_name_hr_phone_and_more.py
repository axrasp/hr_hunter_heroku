# Generated by Django 4.1 on 2022-08-15 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_chat_updated_at_alter_hr_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='hr',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='First name'),
        ),
        migrations.AddField(
            model_name='hr',
            name='is_bot',
            field=models.BooleanField(blank=True, null=True, verbose_name='Bot'),
        ),
        migrations.AddField(
            model_name='hr',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Last name'),
        ),
        migrations.AddField(
            model_name='hr',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone'),
        ),
        migrations.AddField(
            model_name='hr',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 15, 8, 59, 9, 100036, tzinfo=datetime.timezone.utc), verbose_name='Когда обновлялся'),
        ),
        migrations.AlterField(
            model_name='hr',
            name='tg_id',
            field=models.CharField(max_length=20, null=True, verbose_name='Tg ID'),
        ),
        migrations.AlterField(
            model_name='hr',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 15, 8, 59, 9, 100595, tzinfo=datetime.timezone.utc), verbose_name='Дата обновления'),
        ),
    ]