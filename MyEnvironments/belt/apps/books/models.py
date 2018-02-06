# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..users.models import *
# Create your models here.
class BookManager(models.Manager):
    def validate_book_and_review(self, post, user_id):
        errors = []
        if post['title'] == '':
            errors.append('Title cannot be blank')

        if post['review'] == '':
            errors.append('Review cannot be blank')

        if post['score'] =='':
            errors.append('score cannot be blank')

        elif int(post['score']) > 5 or int(post['score']) < 1:
            errors.append('score must be between 1 and 5')

        if 'list_author' not in post and post['new_author']== '':
            errors.append('you either select an author or create a new one')

        elif 'list_author' in post and post['new_author'] != '':
            errors.append('you may only select one author')

        elif 'list_author' in post:
            author = Author.objects.get(id = post['list_author'])
        else:
            author = Author.objects.create(name= post['new_author'])
        if not errors:
            book=  Book.objects.create(
                title=post['title'],
                author=author
            )
            Review.objects.create(
                review=post['review'],
                score =post['score'],
                book=book,
                user= User.objects.get(id=user_id)
            )
            return {'status': True, 'book_id':book.id }
        else:
            return{'status': False, 'errors' : errors}

class ReviewManager(models.Manager):
    def validate_review(self, post, user_id, book_id):
        errors = []
        if post['review'] == "":
            errors.append('Review cannot')
        if post['score'] =='':
            errors.append('score cannot be blank')

        elif int(post['score']) > 5 or int(post['score']) < 1:
            errors.append('score must be between 1 and 5')

        if not errors:
            Review.objects.create(
                review=post['review'],
                score =post['score'],
                book= Book.objects.get(id=book_id),
                user= User.objects.get(id=user_id),
            )
            return {'status':True}
        else:
            return{ 'status': False, 'errors': errors}
class Author(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add = True)

class Book(models.Model):
    title = models.CharField(max_length= 255)
    author = models.ForeignKey (Author, related_name ="books")
    created_at = models.DateTimeField(auto_now_add =  True)
    updated_at =  models .DateTimeField(auto_now = True)
    objects = BookManager()

class Review(models.Model):
    review = models.TextField()
    score = models.IntegerField()
    book = models.ForeignKey(Book, related_name='reviews')
    user = models.ForeignKey(User,related_name = 'reviews')
    created_at = models.DateTimeField(auto_now_add =  True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ReviewManager()

    

