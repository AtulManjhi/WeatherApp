from django.shortcuts import render
import requests
import datetime
import pytz

# Create your views here.

def index(request):
    context = {}
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=your-id'
    url2 = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely&units=metric&appid=your-id'

    if request.GET.get('city'):
        city = request.GET.get('city')

        try:
            r1 = requests.get(url.format(city)).json()
            
            lon = r1['coord']['lon']
            lat = r1['coord']['lat']

            r2 = requests.get(url2.format(lat,lon)).json() 
            
            dir = ["N","NE","NE","NE","E","SE","SE","SE","S","SW","SW","SW","W","NW","NW","NW","N"]
            city_weather = {
                'city': r1['name'],
                'country': r1['sys']['country'],
                'temperature': '{:.1f}'.format(r1['main']['temp']),
                'description': r1['weather'][0]['description'],
                'main': r1['weather'][0]['main'],
                'min_temp': '{:.1f}'.format(r1['main']['temp_min']),
                'max_temp': '{:.1f}'.format(r1['main']['temp_max']),
                'pressure': r1['main']['pressure'],
                'humidity': r1['main']['humidity'],
                'feels_like': '{:.1f}'.format(r1['main']['feels_like']),
                'uvi' : '{:.0f}'.format(r2['current']['uvi']),
                'windspeed': r2['current']['wind_speed'],
                'icon': r1['weather'][0]['icon'],
                'morning': '{:.1f}'.format(r2['daily'][0]['temp']['morn']),
                'day': '{:.1f}'.format(r2['daily'][0]['temp']['day']),
                'eve': '{:.1f}'.format(r2['daily'][0]['temp']['eve']),
                'night': '{:.1f}'.format(r2['daily'][0]['temp']['night']),
                'dew': '{:.0f}'.format(r2['daily'][0]['dew_point'])
            }
            city_weather['timezone'] = r2['timezone'].replace('_',' ')
            wind_deg = r2['current']['wind_deg']
            time0 = r2['daily'][0]['dt']
            tz = r2['timezone']
            time = datetime.datetime.fromtimestamp(time0)
            act_time = time.astimezone(pytz.timezone(tz))
            z0 = act_time.strftime('%a, %b %d')
            city_weather['time'] = z0
            
            ss = r2['daily'][0]['sunset']
            tz = r2['timezone']
            ss_time = datetime.datetime.fromtimestamp(ss)
            act_time = ss_time.astimezone(pytz.timezone(tz))
            z = act_time.strftime('%I:%M %p')
            city_weather['sunset'] = z
            
            sr = r2['daily'][0]['sunrise']
            sr_time = datetime.datetime.fromtimestamp(sr)
            act_time = sr_time.astimezone(pytz.timezone(tz))
            z = act_time.strftime('%I:%M %p')
            city_weather['sunrise'] = z

            index = wind_deg % 360
            index = round(index/22.5)+1
            if index > 16:
                index = 16
            city_weather['winddir'] = dir[index]

            forecast1 = {
                'tempday': '{:.1f}'.format(r2['daily'][1]['temp']['day']),
                'tempnight': '{:.1f}'.format(r2['daily'][1]['temp']['night']),
                'tempmorn': '{:.1f}'.format(r2['daily'][1]['temp']['morn']),
                'tempeve': '{:.1f}'.format(r2['daily'][1]['temp']['eve']),
                'max': '{:.1f}'.format(r2['daily'][1]['temp']['max']),
                'min': '{:.1f}'.format(r2['daily'][1]['temp']['min']),
                'main': r2['daily'][1]['weather'][0]['main'],
                'desc': r2['daily'][1]['weather'][0]['description'],
                'icon': r2['daily'][1]['weather'][0]['icon'],
                'humidity': r2['daily'][1]['humidity'],
                'pressure': r2['daily'][1]['pressure'],
                'windspeed': r2['daily'][1]['wind_speed'],
                'uvi': '{:.0f}'.format(r2['daily'][1]['uvi']),
                'dew': '{:.0f}'.format(r2['daily'][1]['dew_point'])
            }
            wind_deg1 = r2['daily'][1]['wind_deg']
            time1 = r2['daily'][1]['dt']
            tz = r2['timezone']
            time = datetime.datetime.fromtimestamp(time1)
            act_time = time.astimezone(pytz.timezone(tz))
            z1 = act_time.strftime('%a, %b %d')
            forecast1['time'] = z1

            ss = r2['daily'][1]['sunset']
            ss_time = datetime.datetime.fromtimestamp(ss)
            act_time = ss_time.astimezone(pytz.timezone(tz))
            z = act_time.strftime('%I:%M %p')
            forecast1['sunset'] = z
            
            sr = r2['daily'][1]['sunrise']
            sr_time = datetime.datetime.fromtimestamp(sr)
            act_time = sr_time.astimezone(pytz.timezone(tz))
            z = act_time.strftime('%I:%M %p')
            forecast1['sunrise'] = z

            index = wind_deg1 % 360
            index = round(index/22.5)+1
            forecast1['winddir'] = dir[index]

            forecast2 = {
                'tempday': '{:.1f}'.format(r2['daily'][2]['temp']['day']),
                'tempnight': '{:.1f}'.format(r2['daily'][2]['temp']['night']),
                'tempmorn': '{:.1f}'.format(r2['daily'][2]['temp']['morn']),
                'tempeve': '{:.1f}'.format(r2['daily'][2]['temp']['eve']),
                'max': '{:.1f}'.format(r2['daily'][2]['temp']['max']),
                'min': '{:.1f}'.format(r2['daily'][2]['temp']['min']),
                'main': r2['daily'][2]['weather'][0]['main'],
                'desc': r2['daily'][2]['weather'][0]['description'],
                'icon': r2['daily'][2]['weather'][0]['icon'],
                'humidity': r2['daily'][2]['humidity'],
                'pressure': r2['daily'][2]['pressure'],
                'windspeed': r2['daily'][2]['wind_speed'],
                'uvi': '{:.0f}'.format(r2['daily'][2]['uvi']),
                'dew': '{:.0f}'.format(r2['daily'][2]['dew_point'])
            }
            wind_deg2 = r2['daily'][2]['wind_deg']
            time2 = r2['daily'][2]['dt']
            tz = r2['timezone']
            time = datetime.datetime.fromtimestamp(time2)
            act_time = time.astimezone(pytz.timezone(tz))
            z2 = act_time.strftime('%a, %b %d')
            forecast2['time'] = z2

            ss = r2['daily'][2]['sunset']
            ss_time = datetime.datetime.fromtimestamp(ss)
            act_time = ss_time.astimezone(pytz.timezone(tz))
            z = act_time.strftime('%I:%M %p')
            forecast2['sunset'] = z
            
            sr = r2['daily'][2]['sunrise']
            sr_time = datetime.datetime.fromtimestamp(sr)
            act_time = sr_time.astimezone(pytz.timezone(tz))
            z = act_time.strftime('%I:%M %p')
            forecast2['sunrise'] = z

            index = wind_deg2 % 360
            index = round(index/22.5)+1
            forecast2['winddir'] = dir[index]

            forecast3 = {
                'tempday': '{:.1f}'.format(r2['daily'][3]['temp']['day']),
                'tempnight': '{:.1f}'.format(r2['daily'][3]['temp']['night']),
                'tempmorn': '{:.1f}'.format(r2['daily'][3]['temp']['morn']),
                'tempeve': '{:.1f}'.format(r2['daily'][3]['temp']['eve']),
                'max': '{:.1f}'.format(r2['daily'][3]['temp']['max']),
                'min': '{:.1f}'.format(r2['daily'][3]['temp']['min']),
                'main': r2['daily'][3]['weather'][0]['main'],
                'desc': r2['daily'][3]['weather'][0]['description'],
                'icon': r2['daily'][3]['weather'][0]['icon'],
                'humidity': r2['daily'][3]['humidity'],
                'pressure': r2['daily'][3]['pressure'],
                'windspeed': r2['daily'][3]['wind_speed'],
                'uvi': '{:.0f}'.format(r2['daily'][3]['uvi']),
                'dew': '{:.0f}'.format(r2['daily'][3]['dew_point'])
            }
            wind_deg3 = r2['daily'][3]['wind_deg']
            time3 = r2['daily'][3]['dt']
            tz = r2['timezone']
            time = datetime.datetime.fromtimestamp(time3)
            act_time = time.astimezone(pytz.timezone(tz))
            z3 = act_time.strftime('%a, %b %d')
            forecast3['time'] = z3

            ss = r2['daily'][3]['sunset']
            tz = r2['timezone']
            ss_time = datetime.datetime.fromtimestamp(ss)
            act_time = ss_time.astimezone(pytz.timezone(tz))
            z = act_time.strftime('%I:%M %p')
            forecast3['sunset'] = z
            
            sr = r2['daily'][3]['sunrise']
            sr_time = datetime.datetime.fromtimestamp(sr)
            act_time = sr_time.astimezone(pytz.timezone(tz))
            z = act_time.strftime('%I:%M %p')
            forecast3['sunrise'] = z

            index = wind_deg3 % 360
            index = round(index/22.5)+1
            forecast3['winddir'] = dir[index]

            forecast4 = {
                'tempday': '{:.1f}'.format(r2['daily'][4]['temp']['day']),
                'tempnight': '{:.1f}'.format(r2['daily'][4]['temp']['night']),
                'tempmorn': '{:.1f}'.format(r2['daily'][4]['temp']['morn']),
                'tempeve': '{:.1f}'.format(r2['daily'][4]['temp']['eve']),
                'max': '{:.1f}'.format(r2['daily'][4]['temp']['max']),
                'min': '{:.1f}'.format(r2['daily'][4]['temp']['min']),
                'main': r2['daily'][4]['weather'][0]['main'],
                'desc': r2['daily'][4]['weather'][0]['description'],
                'icon': r2['daily'][4]['weather'][0]['icon'],
                'humidity': r2['daily'][4]['humidity'],
                'pressure': r2['daily'][4]['pressure'],
                'windspeed': r2['daily'][4]['wind_speed'],
                'uvi': '{:.0f}'.format(r2['daily'][4]['uvi']),
                'dew': '{:.0f}'.format(r2['daily'][4]['dew_point'])
            }
            wind_deg4 = r2['daily'][4]['wind_deg']
            time4 = r2['daily'][4]['dt']
            tz = r2['timezone']
            time = datetime.datetime.fromtimestamp(time4)
            act_time = time.astimezone(pytz.timezone(tz))
            z4 = act_time.strftime('%a, %b %d')
            forecast4['time'] = z4

            ss = r2['daily'][4]['sunset']
            ss_time = datetime.datetime.fromtimestamp(ss)
            act_time = ss_time.astimezone(pytz.timezone(tz))
            z = act_time.strftime('%I:%M %p')
            forecast4['sunset'] = z
            
            sr = r2['daily'][4]['sunrise']
            sr_time = datetime.datetime.fromtimestamp(sr)
            act_time = sr_time.astimezone(pytz.timezone(tz))
            z = act_time.strftime('%I:%M %p')
            forecast4['sunrise'] = z

            index = wind_deg4 % 360
            index = round(index/22.5)+1
            forecast4['winddir'] = dir[index]

            tz = r2['timezone']
            x = pytz.timezone(tz)
            act_time = datetime.datetime.now(x)
            time_now = act_time.strftime('%B %d, %Y  %I : %M %p')
            
            context['city_weather'] = city_weather
            context['forecast1'] = forecast1
            context['forecast2'] = forecast2
            context['forecast3'] = forecast3
            context['forecast4'] = forecast4
            context['time_now'] = time_now
            return render(request,'main/success.html', context)

        except:
            return render(request,'main/error.html', context)
   
    else:
        return render(request,'main/welcome.html',context)
