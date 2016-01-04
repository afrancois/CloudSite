from django.utils.encoding import smart_unicode
from rest_framework import renderers
from CloudApi.models import CurrentState
from CloudApi.liveweather import OpenWeatherMap

class PlainTextRenderer(renderers.BaseRenderer):
    media_type = 'text/plain'
    format = 'iot'
    map = None
    charset = 'iso-8859-1'

    def __init__(self):
        renderers.BaseRenderer.__init__(self)
        self.map = OpenWeatherMap()




    def render(self, data, media_type=None, renderer_context=None):
        if isinstance(data, dict):
            return self.iot_output(data).encode(self.charset)
        if isinstance(data, (list, tuple)):
            out = ''
            for i in range(len(data)):
                out = "{}{} {}\n".format(out,data[i]['cloud_slug'],self.iot_output(data[i]))
            return out.encode(self.charset)
        return data

    def iot_output(self,data):
        parts = data['position'].rsplit(',')
        try:
            latitude = parts[0]
        except IndexError:
            latitude = '0.0'
        try:
            longitude = parts[1]
        except IndexError:
            longitude = '0.0'

        self.map.set_location(lat=latitude,lon=longitude)

        if data['cloud_state'] == CurrentState.RGB:
            r,g,b = self.HTMLColorToRGB(data['cloud_rgb'])
            return '{} {} {} {}'.format(data['cloud_state'],r,g,b)
        if data['cloud_state'] == CurrentState.OUTSIDE:
            outside = self.map.update()
            return '{} {}'.format(data['cloud_state'],outside)
        return '{} {}'.format(data['cloud_state'],data['cloud_state'])

    def HTMLColorToRGB(self,colorstring):
        """ convert #RRGGBB to an (R, G, B) tuple """
        colorstring = colorstring.strip()
        if colorstring[0] == '#': colorstring = colorstring[1:]
        if len(colorstring) != 6:
            raise ValueError, "input #%s is not in #RRGGBB format" % colorstring
        r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
        r, g, b = [int(n, 16) for n in (r, g, b)]
        return (r, g, b)
