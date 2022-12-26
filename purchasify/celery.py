import os
from celery import Celery

# Configure celery worker for rabbitMQ broker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'purchasify.settings')
app = Celery('purchasify')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()