import os

from celery import Celery
from django.conf import settings

# Set the default value of the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "product_recommendation_system.settings"
)

# Create a Celery app instance
app = Celery("product_recommendation_system", broker=settings.BROKER_URL)

# Configure the Celery app from the Django settings
app.config_from_object("django.conf:settings")

# Automatically discover task modules in the INSTALLED_APPS setting
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Set the result backend to Redis
app.conf.result_backend = "redis://localhost:6379/0"


@app.task(bind=True)
def debug_task(self):
    """Debug task to print the Celery request."""
    print("Request:", self.request)
