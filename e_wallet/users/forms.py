from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class AddClassToFieldMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-option'


class CustomUserCreationForm(AddClassToFieldMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "icon")


class CustomAuthenticationForm(AddClassToFieldMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")
