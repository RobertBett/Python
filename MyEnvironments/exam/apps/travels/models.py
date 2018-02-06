# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..users.models import User

# Create your models here.
class TravelManager(models.Manager):
    def validate_post(self, post, user_id):
        errors = []
        print post['destination']
        print post['description']
        print post['on']
        print post['to']
        if post['destination'] == '':
            errors.append('Content cannot be blank')
        if post['description'] == '':
            errors.append('Content cannot be blank')
        if not errors:
            Travel.objects.create(
                description = post['description'],
                destination = post['destination'],
                on= post['on'],
                to = post['to'],
                user = User.objects.get(id= user_id)
            )
            return{'status': True}
        else:
            return{'status': False, 'errors':errors }
            
class Travel(models.Model):
    destination = models.TextField(max_length=100)
    description = models.TextField()
    on = models.DateField(null = True)
    to = models.DateField(null = True)
    user = models.ManyToManyField(User, related_name="travels")
    objects = TravelManager()
