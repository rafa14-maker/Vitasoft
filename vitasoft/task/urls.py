from django.urls import path

from . import views

urlpatterns = [
    path("projects/<int:project_id>/tasks/", views.task_list, name="task_list"),
    path("tasks/<int:pk>/", views.task_detail, name="task_detail"),
]
