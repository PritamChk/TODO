from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields import TextField

class User(models.Model):
    USER_SEX_MALE = 'M'
    USER_SEX_FEMALE = 'F'
    USER_SEX_OTHER = 'T'
    USER_SEX = [
        (USER_SEX_MALE,'Male'),
        (USER_SEX_FEMALE,'Female'),
        (USER_SEX_OTHER,'Other'),
    ]
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    user_name = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    gender = models.CharField( max_length=2, choices=USER_SEX, default=USER_SEX_MALE)
    phone_no = models.CharField(max_length=12)
    date_of_joining = models.DateTimeField(auto_now_add=True)

class Todo(models.Model):
    title = models.CharField(max_length= 200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=CASCADE)
    tag = models.ManyToManyField("Tag" )

class Tag(models.Model):
    tag_title = models.CharField(max_length= 50)
    user_tag = models.ForeignKey(User , on_delete= CASCADE )
    