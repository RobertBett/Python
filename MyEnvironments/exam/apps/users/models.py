# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')


class UserManager(models.Manager):

    def validate_login(self, post):
        user = User.objects.filter(email=post['email']).first()
        if user and bcrypt.checkpw(post['password'].encode(), user.password.encode()):
            return { 'status': True, 'user': user}
        else:
            return{'status': False, 'error': 'Invalid Email or Password'}


    def validate_registration(self, post):
        errors = []
        if post['name'] == '':
            errors.append('Bruh Name is too short')
        elif len(post['name']) <3:
            errors.append('Bruh name is too short') 
        if not re.match(NAME_REGEX,post['name']):
            errors.append('Name fields must be letter characters only')        
        if post['email'] == '':
            errors.append('Bruh Email cannot be blank')
        if not re.match(EMAIL_REGEX,post['email']):
            errors.append("invalid email")
        user = User.objects.filter(email=post['email']).first()
        if user:
            errors.append('Bruh Email already in use')
        if len(post['password']) <8:
            errors.append('Bruh Password must be at least eight characters')
        elif post['password'] != post['password_confirmation']:
            errors.append('Bruh Password must match')

        if not errors:
            user = User.objects.create(
                name= post['name'],
                email = post['email'],
                password = bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt(10))
            )
            return { 'status': True, 'user': user}
        else:
            return{'status': False, 'errors': errors}

class User(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password =models.CharField(max_length =255)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()