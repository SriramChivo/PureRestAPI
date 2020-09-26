from .models import pureApi
from django import forms


class ApiForm(forms.ModelForm):
    class Meta:
        model = pureApi
        fields = "__all__"
        exclude = ["user"]
