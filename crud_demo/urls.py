from django.urls import path
from . import views

urlpatterns = [
    path("user/login", views.user_login, name="user_login"),
    path("user/logout", views.user_logout, name="user_logout"),
    path("user/<int:user_id>/books", views.books_list, name="books_list"),
    path("user/<int:user_id>/book_add", views.book_add, name="book_add"),
    path("user/<int:user_id>/book/edit/<int:book_id>", views.book_edit, name="book_edit"),
    path("user/<int:user_id>/book/delete/<int:book_id>", views.book_remove, name="book_remove")
]