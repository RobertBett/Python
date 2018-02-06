# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    age = models.IntegerField(default = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Profile object: {} {} {} {}".format(self.first_name, self.last_name, self.email_address, self.age)
