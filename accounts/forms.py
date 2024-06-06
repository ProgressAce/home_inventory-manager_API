from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomAccount


class CustomAccountCreationForm(UserCreationForm):

    class Meta:
        model = CustomAccount
        fields = ("email",)


class CustomAccountChangeForm(UserChangeForm):

    class Meta:
        model = CustomAccount
        fields = ("email",)
