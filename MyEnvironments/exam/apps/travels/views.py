# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from.models import *
from..users.models import User

# Create your views here.
def index(request):
    context = {
        'travels': Travel.objects.all(),
        'user' : User.objects.get(id = request.session['user_id'])
    }
    return render(request,'travels/index.html', context)

def create(request):
        result = Travel.objects.validate_post(request.POST, request.session['user_id'])
        if result['status'] == False: 
            for error in result['errors']:
                messages.error(request, error)
        return redirect('/travels')

def trip(request,id):
    user = User.objects.exclude(id=int(request.session['user']['id']))
    trip =Travel.objects.get(id = int(id))
    context = {
        'trip': trip,
        'user': user
    }
    return render(request,'travels/profile.html',context)

    
def add(request):
    return render(request,'travels/add.html')

