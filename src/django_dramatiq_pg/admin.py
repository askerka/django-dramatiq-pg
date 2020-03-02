from django.contrib import admin

from .models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'queue_name', 'state',)
    list_filter = ('queue_name', 'state',)