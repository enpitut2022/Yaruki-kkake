from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'yaruki_kkake/index.html')
    
def start(request):
    user_name = {
        "user_name" : request.GET.get("user_name")
    }
    return render(request, 'yaruki_kkake/start.html', user_name)

def start2(request):
    return render(request, 'yaruki_kkake/start2.html')

def doing(request):
    time = {
        "time" : request.GET.get("time")
    }
    print(request.GET)
    return render(request, 'yaruki_kkake/doing.html', time)

def doing2(request):
    return render(request, 'yaruki_kkake/doing2.html')