from django.contrib import admin
from shop.models import Category, Product
from parler.admin import TranslatableAdmin


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    """
    Register category model in admin site
    """
    list_display = ['name', 'slug']

    # prepopulated_fields = {'slug': ('name',)}

    def get_prepopulated_fields(self, request, obj=None):
        """
        Create a method to get prepopulated fields since the model now extends from parler translate table
        :param request:
        :param obj:
        :return prepopulated fields:
        """
        return {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    """
    Register product model in admin site
    """
    list_display = ['name', 'slug', 'price', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'available']

    # prepopulated_fields = {'slug': ('name',)}

    def get_prepopulated_fields(self, request, obj=None):
        """
        Create a method to get prepopulated fields since the model now extends from parler translate table
        :param request:
        :param obj:
        :return prepopulated fields:
        """
        return {'slug': ('name', )}