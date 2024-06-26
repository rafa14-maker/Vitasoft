from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "user", "task", "created_at")
    search_fields = ("content", "user__username", "user__email", "task__title")
    list_filter = ("created_at",)


admin.site.register(Comment, CommentAdmin)
