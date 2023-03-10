from django import forms
from django.utils.translation import gettext_lazy as _


class CartAddProductForm(forms.Form):
    """
    Create a from for adding product to cart
    """
    PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
    # Limit the quantity from 1 up to 20 and user coerce to convert values into integer field type
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label=_('Quantity'))
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
