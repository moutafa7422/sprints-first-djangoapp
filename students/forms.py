from django import forms
from .models import login
class LoginForm(forms.Form):

    class Meta:
        model = login
        fields = '__all__'