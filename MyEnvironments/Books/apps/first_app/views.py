# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def index(request):
    errors = Book.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request,error,extra_tags=tag)
            return redirect('/book/edit/'+id)
        else:
            book: Book.objects.get(id=id)
            book.name = request.POST['name']
            book.desc = request.POST['desc']
            book.save()
            return redirect('/books')
            
            
            