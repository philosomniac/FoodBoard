from django import forms
from foodboard.models import CookEvent


class CookEventForm(forms.ModelForm):
    class Meta:
        model = CookEvent
        fields = ['date', 'recipe']
