from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.

def home(request):
    team=Team.objects.all()
    featured_car=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars=Car.objects.order_by('-created_date').all()
    data={
        "teams": team,
        "cars":featured_car,
        "all_cars":all_cars,
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