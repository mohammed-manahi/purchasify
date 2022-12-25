from django.urls import path, include
from cart import views

app_name = 'cart'

urlpatterns = [
    # Add cart detail  url pattern
    path('', views.cart_detail, name='cart_detail'),
    # Add cart products  url pattern
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    # Add cart remove url pattern
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
