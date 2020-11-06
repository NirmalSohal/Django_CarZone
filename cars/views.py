from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def cars(request):
    cars=Car.objects.order_by('-created_date')
    paginator=Paginator(cars,4)
    page=request.GET.get('page')
    paged_car=paginator.get_page(page)
    model_search=Car.objects.values_list('model',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    body_search=Car.objects.values_list('body_style',flat=True).distinct()
    data={
        'cars':paged_car,
        "model_search":model_search,
        "year_search":year_search,
        "city_search":city_search,
        "body_search":body_search,
    }
    return render(request,'cars/cars.html',data)

def car_detail(request,id):
    single_car=get_object_or_404(Car,pk=id)

    data={
        'single_car':single_car,
    }

    return render(request,'cars/car-detail.html',data)

def search(request):
    cars=Car.objects.all().order_by('-created_date')
    if 'keyword' in request.GET:
        keyword=request.GET.get('keyword')
        if keyword:
            cars=Car.objects.filter(description__icontains=keyword)
    
    if 'model' in request.GET:
        model=request.GET.get('model')
        if model:
            cars=Car.objects.filter(model__iexact=model)

    if 'transmission' in request.GET:
        transmission=request.GET.get('transmission')
        if transmission:
            cars=Car.objects.filter(transmission__iexact=transmission)
    
    if 'year' in request.GET:
        year=request.GET.get('year')
        if year:
            cars=Car.objects.filter(year__iexact=year)

    if 'city' in request.GET:
        city=request.GET.get('city')
        if city:
            cars=Car.objects.filter(city__iexact=city)
    
    '''if 'min_price' and 'max_price' in request.GET:
        min_price=request.GET.get('min_price')
        max_price=request.GET.get('max_price')
        if min_price and max_price:
            cars=Car.objects.filter(price__gte=min_price,price__lte=max_price)'''

    model_search=Car.objects.values_list('model',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    body_search=Car.objects.values_list('body_style',flat=True).distinct()
    transmission_search=Car.objects.values_list('transmission',flat=True).distinct()
    
    data={
        'cars':cars,
        "model_search":model_search,
        "year_search":year_search,
        "city_search":city_search,
        "body_search":body_search,
        "transmission_search":transmission_search,
    }
    return render(request,'cars/search.html',data)