from django.http import HttpResponse
from django.shortcuts import render
import requests

def get_info(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q=Bagalkot&units=metric&apikey=8e9cc41a31f27e09ed71c2c6a46bf4dd'
    fetch_data = requests.get(url)
    print(fetch_data)
    weather_info = fetch_data.json()
    context = {
        'city_name': weather_info['name'],
        'humidity': weather_info['main']['humidity'],
        'wind_speed': weather_info['wind']['speed'],
    }
    return render(request, 'weather_info.html', context)

def show_string(request):
    url = 'https://programming-quotes-api.herokuapp.com/quotes/random'
    fetch_string = requests.get(url)
    rand_string = fetch_string.json()
    context = {
        'randomstring': rand_string['en'],
        'author': rand_string['author'],
    }
    return render(request, 'random_string.html', context)

def word_count(request):
    return render(request, 'input_string.html')

def count_result(request):
    string_item = request.GET['inputtext']
    print('input string is ', string_item)
    data = string_item.split()
    count = {}
    for i in data:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print('count is :',count)
    context = {'count': count,}
    return render(request, 'results_count.html', context)
