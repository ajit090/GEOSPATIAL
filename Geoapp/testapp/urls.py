from django.urls import path
from .views import (CountryListCreateAPIView,CountryRetrieveUpdateDestroyAPIView,CountryNameSearchAPIView,CountryIntersectionAPIView,)


urlpatterns = [
    path('countries/', CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroyAPIView.as_view(), name='country-detail'),
    path('countries/search/', CountryNameSearchAPIView.as_view(), name='country-search'),
    path('countries/intersecting/', CountryIntersectionAPIView.as_view(), name='country-intersecting'),
]