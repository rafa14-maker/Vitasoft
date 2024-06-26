from django.urls import path

from . import views

urlpatterns = [
    path("projects/", views.project_list, name="project_list"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path(
        "projects/<int:project_id>/members/",
        views.project_member_list,
        name="project_member_list",
    ),
    path(
        "projects/members/<int:pk>/",
        views.project_member_detail,
        name="project_member_detail",
    ),
]
