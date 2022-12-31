from django.urls import path
from payment import views
from payment import webhooks
from django.utils.translation import gettext_lazy as _

app_name = 'payment'

urlpatterns = [
    # Add payment process url patterns
    path(_('process/'), views.payment_process, name='process'),
    path(_('completed/'), views.payment_completed, name='completed'),
    path(_('canceled/'), views.payment_canceled, name='canceled'),
    # path('webhook/', webhooks.stripe_webhook, name='stripe-webhook'),
]
