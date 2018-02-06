# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import string
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
    return HttpResponse("hello")
def time(request):
    context = {
    "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'first_app/pages.html',context)

def random_word(n):
    return join(random.word(string.ascii_uppercase + string.digits)get_random_string(length = 14))

def main(request):
    try:
        request.session['tries']
    except keyerror:
        request.session['tries']=0
    return render(request,"first_app/pages.html")

def generate(request):
    request.session['tries']
    request.session['word']= random_word(10)
    return redirect('/')

def reset(request):
    del request.session['tries']
    del request.session['word']
    return redirect('/')