from apps.departments.models import Department, Table, Queue
from django.contrib import admin


class TableInline(admin.TabularInline):
    model = Table
    extra = 0


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'table_count']
    search_fields = ['name']
    readonly_fields = ['table_count']
    inlines = [TableInline]

    def table_count(self, instance):
        return instance.table_set.count()


@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    list_display = ['department', 'queue_number', 'is_priority']
    list_filter = ['department']
    ordering = ['queue_number', 'department']