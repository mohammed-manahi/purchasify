from django.urls import path
from coupon import views

app_name = 'coupons'

urlpatterns = [
    # Add coupon apply url pattern
    path('apply/', views.coupon_apply, name='apply'),
]
