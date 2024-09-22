from django.contrib import admin
from apps.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'completed')
    list_filter = ('completed',)
    search_fields = ('name', 'description')
