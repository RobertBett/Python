# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request,'first_app/index.html')
def words(request):
    now =datetime.now().strftime("%H:%M %p, %B %d, %Y")
    if 'name' not in request.session:
        request.session['name'] =[]
    if 'show_big' in request.POST:
        leaf = 3
    else: 
        leaf = 1
    print type(request.session['name'])
    list_word = {
        'name':request.POST['name'],
        'color':request.POST['color'],
        'show_big':leaf,
        'time':now
    }
    request.session['name'].append(list_word)
    # request.session['name'] = request.POST['name']
    # print request.session['name']
    request.session.modified = True
    return redirect('/')
def clear(request):
    request.session.flush()
    return redirect('/')

# Create your views here.
