# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from ..users.models import User

# Create your views here.
def index(request):
    context = {
        'posts' : Post.objects.all(),
        'user': User.objects.get(id = request.session['user_id'])
    }
    return render(request, 'posts/index.html', context)

def create(request):
        result = Post.objects.validate_post(request.POST, request.session['user_id'])
        if result['status'] == False: 
            for error in result['errors']:
                messages.error(request, error)
        return redirect('/posts')

def create_like(request, post_id):
    current_user = User.objects.get(id=request.session['user_id'])
    post = Post.objects.get(id =post_id)
    post.likes.add(current_user)
    return redirect('/posts')