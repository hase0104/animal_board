from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:page>", views.index, name="index"),
    path("post", views.post, name="post"),
    path("post_list/<int:page>", views.post_list, name="post_list"),
    path("edit/<int:page>", views.edit, name="edit"),
    path("comment", views.comment, name="comment"),
    path("user_login", views.user_login, name="user_login"),
    path("good/<int:page>", views.good, name="good"),
]