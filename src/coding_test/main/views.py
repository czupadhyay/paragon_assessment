from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.core.paginator import Paginator
from django.shortcuts import render

@api_view(['GET'])
def weather(request):
    '''
    This function accepts two optional parameters (date and station) from query strings and filter out
    the objects based on them from Weather Table.
    Pagination is implemented to load the large data (100 data per page)
    '''
    weather_obj = Weather.objects.all()
    if request.GET.get('date') is not None:
        weather_obj=weather_obj.filter(date=request.GET.get('date'))
    if request.GET.get('station') is not None:
        weather_obj=weather_obj.filter(station=request.GET.get('station'))
    p = Paginator(weather_obj, 100)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    serializer = WeatherSerializer(page_obj, many=True)
    return Response({'status':200,'weather_objs':serializer.data})

@api_view(['GET'])
def weather_stats(request):
    '''
    This function accepts two optional parameters (date and station) from query strings and filter out
    the objects based on them from AVGWeather Table.
    Pagination is implemented to load the large data.(100 data per page)
    '''
    stats = AVGWeather.objects.all()
    if request.GET.get('date') is not None:
        stats=stats.filter(date=request.GET.get('date'))
    if request.GET.get('station') is not None:
        stats=stats.filter(station=request.GET.get('station'))
    p = Paginator(stats, 100)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    serializer = AVGWeatherSerializer(page_obj, many=True)
    return Response({'status':200,'weather_stats':serializer.data})

@api_view(['GET'])
def get_yield(request):
    '''
    This function returns the all entries from Yield table.
    Pagination is implemented to load the large data.(100 data per page)
    '''
    stats = Yield.objects.all()
    p = Paginator(stats, 100)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    serializer = YieldSerializer(page_obj, many=True)
    return Response({'status':200,'yield':serializer.data})


def home(request):
    return render(request,'home.html')


    


