"""purchasify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from payment import webhooks

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    # Include url patterns of the cart app
    path(_('cart/'), include('cart.urls', namespace='cart')),
    # Include url patterns of the account app
    path(_('account/'), include('account.urls')),
    # Include url patterns of the order app
    path(_('order/'), include('order.urls', namespace='order')),
    # Include url patterns of the payment app
    path(_('payment/'), include('payment.urls', namespace='payment')),
    # Include url patterns of the coupon app
    path(_('coupon/'), include('coupon.urls', namespace='coupon')),
    # Include url patterns of rosetta third-party library
    path('rosetta/', include('rosetta.urls')),
    # Include url patterns of the shop app
    path('', include('shop.urls', namespace='shop')),
)

# Add stripe webhook outside i18n patterns since stripe is a third party service
urlpatterns += [path('payment/webhook/', webhooks.stripe_webhook, name='stripe-webhook'), ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
