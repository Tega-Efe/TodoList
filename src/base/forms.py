from django import forms

# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()

# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re

# forms.py

class CustomUserCreationForm(UserCreationForm):

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        errors = []

        if password1 and password2 and password1 != password2:
            errors.append("Passwords don't match")

        if len(password1) < 8:
            errors.append("Password must be at least 8 characters long")

        if not re.search(r'[A-Z]', password1):
            errors.append("Password must contain at least one uppercase letter")

        if not re.search(r'\d', password1):
            errors.append("Password must contain at least one digit")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
            errors.append("Password must contain at least one special character")

        if errors:
            raise ValidationError("Password must contain 8 characters, at least 1 digit, 1 uppercase letter & 1 special character")

        return password2
