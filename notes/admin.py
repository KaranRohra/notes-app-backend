from django.contrib import admin
from . import models


@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title',)
