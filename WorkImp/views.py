from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse

from .serializers import WhitelistSerialzer
from .models import Whitelist

#class WhitelistViewSet(view)

def add_to_whitelist(request):
    if request.method == 'POST':
        entry = new Whitelist(request.POST)
        entry.save
        return HttpResponse(200)

def compare_white_list

class WhitelistViewSet(viewsets.ModelViewSet):
    queryset = Whitelist.objects.all().order_by('name')
    serialzer_class = WhitelistSerialzer
