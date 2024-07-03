from celery import shared_task
from urllib import request
from django.contrib.gis.geos import GEOSGeometry
from testapp.models import Country

@shared_task
def update_countries_from_geojson():
    url = '<URL to GeoJSON>'
    response = request.get(url)
    geojson_data = response.json()

    for feature in geojson_data['features']:
        country_name = feature['properties']['name']
        country_geometry = GEOSGeometry(str(feature['geometry']), srid=4326)

        # Update or create country in database
        Country.objects.update_or_create(
            name=country_name,
            defaults={'geometry': country_geometry}
        )