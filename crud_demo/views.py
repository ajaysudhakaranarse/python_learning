from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Book
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, "login successfully!")
                return HttpResponseRedirect('%d/books'%user.id)
        else:
            return HttpResponse("Invalid login details given")        
    else:
        return render(request, "crud_demo/user/login.html")    

def books_list(request, user_id):
    books = Book.objects.filter(user_id=user_id)
    context = {
        "books": books
    }
    return render(request, "crud_demo/book/index.html", context)
