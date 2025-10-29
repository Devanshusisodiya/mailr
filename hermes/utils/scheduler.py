from celery import Celery
from hermes.config import settings

celery_app = Celery(
    "warmup",
    broker=settings.redis_url,
    backend=settings.redis_url
)