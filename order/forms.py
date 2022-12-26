from django import forms
from order.models import Order

class OrderCreateForm(forms.ModelForm):
    """
    Create a form for creating orders
    """
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'post_code', 'city']