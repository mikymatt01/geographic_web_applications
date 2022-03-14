from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Italy
from .serializers import ItalySerializer
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
import json

@api_view(['POST'])
def borders(request):
    data = json.loads(request.POST.dict()['_content'])
    if all(item in ['latitude', 'longitude', 'radius'] for item in list(data.keys())):
        pnt = Point(float(data['longitude']),float(data['latitude']))
        radius = int(data['radius']) #optimal radius > 20, time estimated 2 second
        italy = Italy.objects.filter(mpoly__distance_lt=(pnt, Distance(km=radius)))
        serializer = ItalySerializer(italy, many=True)
        return Response(serializer.data)   
    return Response({'error':'required params latitude, longitude and radius'})

@api_view(['POST'])
def geocoding(request):
    data = json.loads(request.POST.dict()['_content'])
    print(data)
    if all(item in ['latitude', 'longitude'] for item in list(data.keys())):
        pnt = Point(float(data['longitude']),float(data['latitude']))
        italy = Italy.objects.filter(mpoly__contains=pnt)
        serializer = ItalySerializer(italy, many=True)
        return Response(serializer.data)
    return Response({'error':'required params latitude, longitude'})