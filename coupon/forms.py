from django import forms
from django.utils.translation import gettext_lazy as _


class CouponApplyForm(forms.Form):
    """
    Create a form to apply coupon on purchase
    """
    code = forms.CharField(label=_('Coupon'))
