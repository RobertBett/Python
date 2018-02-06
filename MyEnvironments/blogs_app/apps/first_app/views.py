from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display all the list of blogs")
def mail(request):
    context = {
    "email" : "blog@gmail.com",
    "name" : "mike",
    "stuff":["stuff"]
    }
    return render(request, "first_app/index.html", context)
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def wow(request):
    return HttpResponse("fuck yea")
def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print "*"*50
        return redirect("/mail")
    else:
        return redirect("/mail")

def show(request, blog_id):
    print blog_id
    return HttpResponse("placeholder to display blog {}".format(blog_id))

def edit(request, blog_id):
    return HttpResponse("placeholder to edit blog {}".format(blog_id))

def delete(request, blog_id):
    return redirect('/')