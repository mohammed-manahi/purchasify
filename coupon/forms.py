from django import forms


class CouponApplyForm(forms.Form):
    """
    Create a form to apply coupon on purchase
    """
    code = forms.CharField()
