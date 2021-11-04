from django import forms
from django.forms.widgets import HiddenInput
from foodboard.models import CookEvent, User
from django.contrib.auth.forms import UserCreationForm


class CookEventForm(forms.ModelForm):
    class Meta:
        model = CookEvent
        fields = ['date', 'recipe']


class NewUserForm(UserCreationForm):
    registration_code = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['registration_code',
                  'username',
                  'email',
                  'password1',
                  'password2']
        help_texts = {
            'username': None,
            'email': None,
        }

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)

        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
