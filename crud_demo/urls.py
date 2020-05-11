from django.urls import path
from . import views

urlpatterns = [
    path("user/login", views.user_login, name="user_login"),
    path("user/<int:user_id>/books", views.books_list, name="books_list")
]