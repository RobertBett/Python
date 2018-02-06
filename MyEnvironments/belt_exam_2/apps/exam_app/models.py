from __future__ import unicode_literals
from django.db import models
import re,bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
def uni_str_dict(mydict):
  data = {}
  for key, val in mydict.iteritems():
    if key != 'csrfmiddlewaretoken':
      data[key] = str(val)
  return data

class UserManager(models.Manager):
    def makeUser(self, form):
        flag = False
        errors = {}
        data = uni_str_dict(form)
        all_users = User.objects.all()
        try:
            all_users[0].username
            username = all_users[0].username
        except IndexError:
            username = ""
        if len(data['name']) < 2:
            errors['name'] = 'Name must be at least 3 characters'
            flag = True
        if len(data['username']) < 2:
            errors['username'] = 'Username must be at least 3 characters'
            flag = True
        if not data['password'] == data['confirm_password']:
            errors['confirm_password'] = "Password must match!"
            flag = True
        if len(data['password']) < 7:
            errors['password'] = '*Password must be at least 8 characters'
            flag = True
        # if  email == data['email']:
        #     errors['exitsitng'] = "Email already exists!"
        #     flag = True
        try:
            user_input = User.manager.get(username=data['username']) # this line will try to match user_input_email with the database for email
            errors['existing'] = "Username exists in database!!!"
            flag = True
            return (False, errors)
        except Exception:
            pass

        # .... many validations later
        if flag:
          return (False, errors)
        hashed_password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
        this_user = self.create(name=data['name'],username=data['username'],password=hashed_password)
    #     return successfull_reg()
    # def successfull_reg(self,form):
        user = {}
    #     data = uni_str_dict(form)
        # this_user = User.manager.get(email=data['email']) # this line will create a user object from the successfully registered user
        user['username'] = this_user.username # following lines will create key/value pairs in dictionary named user
        user['id'] = this_user.id
        user['name'] = this_user.name
        return (True, user) # this line will send the dictionary user to the views page

    def login(self,form):
        errors={}
        user = {}
        data = uni_str_dict(form)
        flag = False
        try:
            this_user = User.manager.get(username=data['username'])
        except Exception:
            errors['username'] = "Invalid username"
            flag = True
            return (False,errors)
        try:
            user_input = data['password'] # this line will check if the user inputed a password
        except Exception:
            errors['empty_password'] = "Enter password" # this line will create a message in the case that user_input was empty
            flag = True
            return (False, errors) # this line will redirect back to login_and_registration in the case that the user_input does not exist
        hashed_one = this_user.password # this line will retreive the user's existing hashed password

        if not bcrypt.checkpw(user_input.encode(), hashed_one.encode()):
            errors['password'] = 'Invalid password'
            flag = True
        if flag:
            return (False, errors)
        user['username'] = this_user.username
        user['id'] = this_user.id
        user['name'] = this_user.name
        return (True, user)


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    manager = UserManager()
    objects = models.Manager()
    def __repr__(self):
        return "<users object: {} {} {}>".format(self.name, self.username,self.password)
class Trip(models.Model):
    destination = models.CharField(max_length=255)
    desc = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    users = models.ManyToManyField(User,related_name="trips")

# Create your models here.
