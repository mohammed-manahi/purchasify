from purchasify.celery import app as celery_app

# Make sure celery is loaded in initializer when Django starts
__all__ = ['celery_app']
