from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
)
UserModel = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'name': 'username',
                'id': 'username'}
        ),
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'name': 'password',
                'id': 'password'})
    )

    def clean_username(self, *args, **kwargs):
        email = self.cleaned_data.get("username")
        try:
            queryset = UserModel.objects.get(email=email)
            if not queryset.is_active:
                raise forms.ValidationError(
                    ("Usuario inactivo."),
                    code='invalid',
                )
            username = queryset.username
            print(username)
        except UserModel.DoesNotExist:
            raise forms.ValidationError(
                ("Usuario y Contraseña no coiciden."),
                code='invalid',
            )
        return email
