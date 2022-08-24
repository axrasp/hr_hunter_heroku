from django.contrib import admin

from .models import HR, Chat


class HrChatsInline(admin.TabularInline):
    model = Chat.hrs.through
    raw_id_fields = ['hr', 'chat']


@admin.register(HR)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = (
        'tg_id',
        'username',
    )
    readonly_fields = [
        'created_at',
        'updated_at'
    ]
    list_display = (
        'tg_id',
        'username',
        'first_name',
        'last_name',
        'updated_at',
        'phone'
    )
    inlines = [HrChatsInline]


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    search_fields = (
        'tg_id',
        'chat'
    )
    readonly_fields = [
        'created_at',
        'updated_at'
    ]
    list_display = (
        'title',
        'chat_id',
        'updated_at',
    )
    inlines = [HrChatsInline]

