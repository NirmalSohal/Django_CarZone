from django.shortcuts import render
from .models import Team

# Create your views here.

def home(request):
    team=Team.objects.all()
    data={
        "teams": team
    }
    return render(request,'pages/home.html',data)

def about(request):
    team=Team.objects.all()
    data={
        "teams": team
    }
    return render(request,'pages/about.html',data)

def service(request):
    return render(request,'pages/service.html')

def contact(request):
    return render(request,'pages/contact.html')