from django.shortcuts import render
import requests
import json
def home(request):
    if request.method=='POST':
        city=request.POST['city']
        
        url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=d51b20d1a4b9081a18a876339c2042e4'
        r=requests.get(url.format(city)).json()
        print("in\nn\n\n\n\n\n  ")
        print(r)
        c={}
        c['city']=city
        c['weather']=r['weather'][0]['description']
        c['temprature']=r['main']['temp']
        c['humidity']=r['main']['humidity']
        c['country']=r['sys']['country']
        rpt={}
        rpt['c']=c
        return render(request,'home.html',rpt)
    return render(request,'home.html')
