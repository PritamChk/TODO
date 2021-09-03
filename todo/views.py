from django.shortcuts import render
from .models import User

def login(request):
    if request.method == "POST":
        user_name = request.POST["user_name"]
        password = request.POST["user_password"]
        if User.objects.filter(user_name=user_name,password=password).exists():
            user=User.objects.get(user_name=user_name)
            return render(request,"home.html",{"user":user})
    else:
        return render(request,"login.html")

def Registration(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        user_name = request.POST["user_name"]
        password = request.POST["password"]
        phone = request.POST["phone"]
        sex = request.POST["sex"]
        user_exists=User.objects.filter(user_name = user_name).exists()
        if user_exists:
            return render(request,"home.html", {"details":[first_name,last_name,user_name,password,phone,sex]})
        else:
            user=User()
            user.first_name=first_name
            user.last_name=last_name
            user.user_name=user_name
            user.password=password
            user.phone_no=phone
            user.gender=sex
            user.save()
            return render(request,"home.html", {"details":[first_name,last_name,user_name,password,phone,sex]})
    else:
        return render(request,"login.html")

