import os

from celery import Celery
from django.conf import settings

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "product_recommendation_system.settings"
)
app = Celery("sitechecker", broker=settings.BROKER_URL)


app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.result_backend = "redis://localhost:6379/0"


@app.task(bind=True)
def debug_task(self):
    print("Request: " f"{self.request}")
