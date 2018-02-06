from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from ..users.models import User


def current_user(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])


def home(request):
    context = {
        'current_user': current_user(request)
    }
    return render(request, 'books/home.html', context)


def new(request):
    context = {
        'authors': Author.objects.all
    }
    return render(request, 'books/new.html', context)

def create(request):
    if request.method == 'POST':
        result = Book.objects.validate_book_and_review(request.POST, request.session['user_id'])
        if result['status']== True:
            return redirect("/books/{}".format(result['book_id']))
        else:
            for error in result['errors']:
                messages.error(request, error)
    return redirect('/books/new')

def show(request, book_id):
    book =Book.objects.get(id=book_id)
    context = {
        'book': book,
        'reviews': book.reviews.all(),
    }
    return render(request, 'books/show.html', context)
def create_review(request, book_id):
    if request.method =="POST":
        result = Review.objects.validate_review(request.POST, request.session['user_id'], book_id)
        if result['status']== False:
            for error in result['errors']:
                messages.error(request, error)
        return redirect("/books/{}".format(book_id))


