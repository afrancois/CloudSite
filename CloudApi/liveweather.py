import httplib
import json
from CloudApi.models import CurrentState

class OpenWeatherMap:
    host = 'api.openweathermap.org'
    url = '/data/2.5/weather'
    query = ''
    appid = '474d0fc6d7d8d26c9f624418dd7f34f0'
    mapping = {     
        '01d': CurrentState.BLUE_SKY,
        '01n': CurrentState.NIGHT,
        '02d': CurrentState.BLUE_SKY,
        '02n': CurrentState.NIGHT,
        '03d': CurrentState.OVERCAST,
        '03n': CurrentState.OVERCAST,
        '04d': CurrentState.OVERCAST,
        '04n': CurrentState.OVERCAST,
        '09d': CurrentState.OVERCAST,
        '09n': CurrentState.OVERCAST,
        '10d': CurrentState.OVERCAST,
        '10n': CurrentState.OVERCAST,
        '50d': CurrentState.OVERCAST,
        '50n': CurrentState.OVERCAST,
        '11d': CurrentState.LIGHTNING,
        '11n': CurrentState.LIGHTNING,
        '13d': CurrentState.SNOW,
        '13n': CurrentState.SNOW,}

    def set_location(self,loc=None,lat=None,lon=None):
        if(loc == None and lat == None and lon == None):
            return
        if(loc != None):
            self.query = '?q={}&appid={}'.format(loc,self.appid)
            return
        self.query = '?lat={}&lon={}&appid={}'.format(lat,lon,self.appid)
        return

    def update(self):
        conn = httplib.HTTPConnection(self.host,80)
        conn.request("GET",self.url+self.query)
        resp = conn.getresponse()
        data = resp.read()
        print(data)
        weather = json.loads(data)
        icon = weather['weather'][0]["icon"]
        dt = weather['dt']
        sunrise = weather['sys']['sunrise']
        sunset = weather['sys']['sunset']
        if(sunrise-dt > 0 and sunrise-dt < 1800) or (sunset-dt>0 and sunset-dt<1800):
            return CurrentState.GOLDEN
        if icon in self.mapping:
            return self.mapping[icon]

        return CurrentState.BLUE_SKY
        

        

