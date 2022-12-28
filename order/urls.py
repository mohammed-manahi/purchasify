from django.urls import path, include
from order import views

app_name = 'order'

urlpatterns = [
    # Add order create url pattern
    path('create/', views.order_create, name='order_create'),
    # Add custom order detail in admin site
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    # Add custom order invoice in admin site to generate invoice pdf
    path('admin/order/<int:order_id>/pdf', views.admin_order_pdf, name='admin_order_pdf'),

]
