import csv
import datetime
from django.http import HttpResponse
from django.contrib import admin
from order.models import Order, OrderItem


def export_to_csv(modeladmin, request, queryset):
    """
    Create custom action in admin site for order model to generate csv file of orders
    :param modeladmin:
    :param request:
    :param queryset:
    :return orders csv file:
    """
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'
    # Declare the content type of the response as csv file
    response = HttpResponse(content_type='text/csv')
    # Indicate that the response includes attached file
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)
    # Use get_fields() to get model fields and exclude any relationship with other models
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write the header row
    writer.writerow([field.verbose_name for field in fields])
    # Write the actual data
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


# Define the action name using the short description attribute
export_to_csv.short_description = 'Export to CSV'


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
    # Add the custom action to generate csv file here
    actions = [export_to_csv]
