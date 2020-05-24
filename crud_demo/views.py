from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book
from django.urls import reverse
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, "login successfully...!")
                return HttpResponseRedirect('%d/books'%user.id)
        else:
            messages.error(request, "Invalid username/password")
            return render(request, "crud_demo/user/login.html")        
    else:
        return render(request, "crud_demo/user/login.html")

def user_logout(request):
    logout(request)
    messages.success(request, "logout successfully...!")
    return HttpResponseRedirect(reverse("crud_demo:user_login"))

@login_required(login_url = "crud_demo:user_login")
def books_list(request, user_id):
    books = Book.objects.filter(user_id = user_id)
    context = {
        "books": books,
        "user_id": user_id
    }
    return render(request, "crud_demo/book/index.html", context)

@login_required(login_url = "crud_demo:user_login")
def book_add(request, user_id):
    context = {
        "user_id": user_id
    }
    if request.method == 'POST':
        book_name   = request.POST.get("book_name")
        author_name = request.POST.get("author_name")
        book = Book(name = book_name, author = author_name, user_id = user_id)
        book.save()
        messages.success(request, "Book created successfully...!")
        return HttpResponseRedirect(reverse("crud_demo:books_list", args = (user_id,)))
    else:
        return render(request, "crud_demo/book/create.html", context)

@login_required(login_url = "crud_demo:user_login")
def book_edit(request, user_id, book_id):
    book = load_book(user_id, book_id)
    context = {"book": book, "user_id": user_id}
    if request.method == 'POST':
        book.name   = request.POST.get("book_name")
        book.author = request.POST.get("author_name")
        book.save()
        messages.success(request, "Book updated successfully...!")
        return HttpResponseRedirect(reverse("crud_demo:books_list", args = (user_id,)))
    else:
        return render(request, "crud_demo/book/edit.html", context)

@login_required(login_url = "crud_demo:user_login")    
def book_remove(request, user_id, book_id):
    book = load_book(user_id, book_id)
    book.delete() 
    messages.success(request, "Book deleted successfully...!")
    return HttpResponseRedirect(reverse("crud_demo:books_list", args = (user_id,)))
    
def load_book(user_id, book_id):
    return Book.objects.filter(user_id = user_id, id = book_id).first()

