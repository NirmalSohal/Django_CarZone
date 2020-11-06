from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.

def home(request):
    team=Team.objects.all()
    featured_car=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars=Car.objects.order_by('-created_date').all()
    #search_fields=Car.objects.values('model','city','year','body_style').distinct()
    model_search=Car.objects.values_list('model',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    body_search=Car.objects.values_list('body_style',flat=True).distinct()
    data={
        "teams": team,
        "cars":featured_car,
        "all_cars":all_cars,
        "model_search":model_search,
        "year_search":year_search,
        "city_search":city_search,
        "body_search":body_search,
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