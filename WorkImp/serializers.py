from rest_framework import serializers
from .models import Whitelist

class WhitelistSerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Whitelist
        fields = ['name', 'url']
