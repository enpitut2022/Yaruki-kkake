from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'yaruki_kkake/index.html')
    
def start(request):
    return render(request, 'yaruki_kkake/start.html')

def start2(request):
    return render(request, 'yaruki_kkake/start2.html')

def doing(request):
    return render(request, 'yaruki_kkake/doing.html')