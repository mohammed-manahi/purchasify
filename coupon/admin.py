from django.contrib import admin
from coupon.models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    """
    Register coupon model in admin site
    """
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']
