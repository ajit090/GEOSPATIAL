from _future_ import absolute_import, unicode_literals # type: ignore
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Geoapp.settings')

app = Celery('Geoapp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()