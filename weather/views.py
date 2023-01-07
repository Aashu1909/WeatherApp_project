from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from . import getWeather 
from collections import defaultdict
def home(request):
    return render(request,'home.html')

def getWeather_city(request):
    print('getWeatherCity')
    if request.method!='POST':
        return HttpResponse("Invalid Method")
    else:
        cityName=request.POST.get('cityName')
        print(cityName)
        params=getWeather.getWeather_by_city(cityName)
        main=['haze','clear','clouds','snow','rain','thunderstorm']
        for l in main: params[l]=False
        haze=['mist','smoke','dust','fog','sand','Ash','tornado','haze']
        if params['condition'] in haze: params['haze']=True
        elif params['condition']=='snow':params['snow']=True
        elif params['condition']=='clear': params['clear']=True
        elif params['condition']=='clouds': params['clouds']=True
        elif params['condition'] in ['rain','drizzle']: params['rain']=True
        elif params['condition']=='thunderstorm' : params['storm']=True
    return render(request,'temp.html',params)


def getWeather_crd(request):
    if request.method!='POST':
        return HttpResponse("Invalid Method")
    params=getWeather.getWeather_by_crd()
    if params=='invalid': return HttpResponse('invalid entry')
    main=['haze','clear','clouds','snow','rain','thunderstorm']
    for l in main: params[l]=False
    haze=['mist','smoke','dust','fog','sand','Ash','tornado','haze']
    if params['condition'] in haze: params['haze']=True
    elif params['condition']=='snow':params['snow']=True
    elif params['condition']=='clear': params['clear']=True
    elif params['condition']=='clouds': params['clouds']=True
    elif params['condition'] in ['rain','drizzle']: params['rain']=True
    elif params['condition']=='thunderstorm' : params['storm']=True
    print(params)
    return render(request,'temp.html',params)
