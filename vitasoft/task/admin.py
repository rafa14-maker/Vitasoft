from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "priority",
        "assigned_to",
        "project",
        "created_at",
        "due_date",
    )
    search_fields = (
        "title",
        "description",
        "assigned_to__username",
        "assigned_to__email",
        "project__name",
    )
    list_filter = ("status", "priority", "created_at", "due_date")


admin.site.register(Task, TaskAdmin)
