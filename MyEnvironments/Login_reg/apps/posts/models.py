# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..users.models import User

# Create your models here.
class PostManager(models.Manager):
    def validate_post(self, post, user_id):
        errors = []
        print post['contents']
        if post['contents'] == '':
            errors.append('Content cannot be blank')
        if not errors:
            Post.objects.create(
                contents = post['contents'], 
                user = User.objects.get(id= user_id)
            )
            return{'status': True}
        else:
            return{'status': False, 'errors':errors }
            
class Post(models.Model):
    contents = models.TextField()
    user = models.ForeignKey(User, related_name="posts")
    likes = models.ManyToManyField(User, related_name= "posts_liked")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = PostManager()
