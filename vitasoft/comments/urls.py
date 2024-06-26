from django.urls import path

from . import views

urlpatterns = [
    path("tasks/<int:task_id>/comments/", views.comment_list, name="comment_list"),
    path("comments/<int:pk>/", views.comment_detail, name="comment_detail"),
]
