from rest_framework import viewsets
from rest_framework import serializers
from .models import CurrentState
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .renderers import PlainTextRenderer


class CloudStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentState
        fields = '__all__'

class CloudStateViewset(viewsets.ModelViewSet):
    lookup_field = "cloud_slug"
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, PlainTextRenderer)
    queryset = CurrentState.objects.all()
    serializer_class= CloudStateSerializer