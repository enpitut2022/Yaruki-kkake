from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    return render(request, 'yaruki_kkake/index.html')
    
def start(request):
    user_name = {
        "user_name" : request.GET.get("user_name")
    }
    user = User(name=user_name["user_name"])
    user.save()
    request.session['user_name'] = user_name["user_name"]
    return render(request, 'yaruki_kkake/start.html', user_name)

def start2(request):
    return render(request, 'yaruki_kkake/start2.html')

def doing(request):
    context = {
        "time" : request.GET.get("time"),
        "user_name" : request.session['user_name']
    }
    print(request.GET)
    return render(request, 'yaruki_kkake/doing.html', context)

def doing2(request):
    return render(request, 'yaruki_kkake/doing2.html')