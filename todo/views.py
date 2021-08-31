from django.shortcuts import render

def login(request):
    return render(request,"login.html")

def Registration(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        user_name = request.POST["user_name"]
        password = request.POST["password"]
        phone = request.POST["phone"]
        sex = request.POST["sex"]
    
        return render(request,"home.html", {"details":[first_name,last_name,user_name,password,phone,sex]})
    else:
        return render(request,"login.html")
