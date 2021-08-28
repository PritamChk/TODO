from django.db import models

class User(models.Model):
    
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    user_name = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=15)
    phone_no = models.CharField(max_length=12)
    date_of_joining = models.DateTimeField(auto_now_add=True)
    


