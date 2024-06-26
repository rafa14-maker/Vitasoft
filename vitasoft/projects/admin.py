from django.contrib import admin

from .models import Project, ProjectMember


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at")
    search_fields = ("name", "owner__username", "owner__email")
    list_filter = ("created_at",)


class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ("project", "user", "role")
    search_fields = ("project__name", "user__username", "user__email")
    list_filter = ("role",)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMember, ProjectMemberAdmin)
