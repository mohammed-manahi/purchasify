from django.contrib import admin
from order.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """
    Include order item in order site admin as an inline display
    """
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Register order model in admin site
    """
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'post_code', 'city', 'created_at',
                    'updated_at']
    list_filter = ['created_at', 'updated_at', 'paid']
    inlines = [OrderItemInline]
