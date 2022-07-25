import django.shortcuts import render

def index(request):
	return render(request, "yaruki_kkake/index.html")