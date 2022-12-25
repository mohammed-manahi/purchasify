from django import forms
from account.models import User


class UserRegistrationForm(forms.ModelForm):
    """
     Create user registration form to register new users
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        """
         Set form model and fields required rather than password and repeat password field
         """
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        """
        Check if password and repeat password fields match and its pattern starts with clean_fieldname
        """
        data = self.cleaned_data
        if data["password"] != data["password2"]:
            raise forms.ValidationError("Passwords don't match")
        return data["password2"]


class UserEditForm(forms.ModelForm):
    """
    Create user edit form to edit default user fields
    """
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


