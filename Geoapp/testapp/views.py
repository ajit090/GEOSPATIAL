from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Country
from .serializers import CountrySerializer
from django.db.models import Q
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db.models.functions import Intersection
from django.views.generic import TemplateView


def home(request):
    return render(request, 'home.html')


class CountryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryNameSearchAPIView(generics.ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Country.objects.filter(name__icontains=query)

class CountryIntersectionAPIView(generics.ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        india_geometry = GEOSGeometry('POLYGON((68.186248 7.106458, 97.415946 35.674545, 77.582121 35.717742, 68.186248 7.106458))', srid=4326)
        return Country.objects.filter(geometry__intersects=india_geometry)
