# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    age = models.IntegerField(default = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Users object: {} {} {} {}".format(self.first_name, self.last_name, self.email_address, self.age)
class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name'])<1:
            errors['name']='Book name should be more than 5 characters'
        if len(postData['desc'])<10:
            errors['desc']='Book desc should be more than 10 characters'
        return errors
class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(User, related_name="uploaded_books",null= True)
    liked_by = models.ManyToManyField(User,related_name="liked_books",null= True)

    object = BookManager()

    def __str__(self):
        return "<Book object: {} {} ".format(self.name, self.desc)
