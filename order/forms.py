from django import forms
from order.models import Order
from localflavor.us.forms import USZipCodeField


class OrderCreateForm(forms.ModelForm):
    """
    Create a form for creating orders
    """
    post_code = USZipCodeField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'post_code', 'city']
