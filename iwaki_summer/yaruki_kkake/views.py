from django.shortcuts import render
from .models import User, Rank

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
    user = User.objects.filter(name=context["user_name"])
    print(user[0].id)
    if not Rank.objects.filter(time=context["time"]).exists():
        time = Rank(
            name=user[0],
            time=context["time"]
        )
        time.save()
    qs = Rank.objects.order_by("time")
    context["object_list"] = qs
    return render(request, 'yaruki_kkake/doing.html', context)

def doing2(request):
    return render(request, 'yaruki_kkake/doing2.html')

def ajax(request):
    return render(request, 'yaruki_kkake/ajax.html')