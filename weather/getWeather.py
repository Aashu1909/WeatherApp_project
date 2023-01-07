from geopy.geocoders import Nominatim
import requests
import geocoder

def getWeather_by_city(city):
    print('city:',city)
    geoLocation=Nominatim(user_agent='geoapiExercises')
    location=geoLocation.geocode(city)
    try:
        api=f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid=b43f10ee28457f4de623661a00c68baf"
        json_data=requests.get(api).json()
        city=json_data['name']
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temperature=int(json_data['main']['temp']-272.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']
        country=json_data['sys']['country']
        feels_like=json_data['main']['feels_like']-272.15
    except Exception as e:
        return 'invalid'
    return {'city':city, 'feels_like':round(feels_like,2),'country':country, 'condition':condition.lower(),
    'wind':wind,'description':description,'temperature':temperature,'pressure':pressure,'humidity':humidity}

def getWeather_by_crd():
    g = geocoder.ip('me')
    lat,long=g.latlng
    try:
        api=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=b43f10ee28457f4de623661a00c68baf"
        json_data=requests.get(api).json()
        city=json_data['name']
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temperature=int(json_data['main']['temp']-272.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']
        country=json_data['sys']['country']
        feels_like=json_data['main']['feels_like']-272.15
    except Exception as e:
        print('Weather App','invalid entry')
    return {'city':city, 'feels_like':round(feels_like,2),'country':country, 'condition':condition.lower(),
    'wind':wind,'description':description,'temperature':temperature,'pressure':pressure,'humidity':humidity}


