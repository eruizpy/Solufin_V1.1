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

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("username")
        passwd = self.cleaned_data.get("password")
        try:
            queryset = UserModel.objects.get(email=email)
            user = authenticate(
                username=queryset.username,
                password=passwd,
            )

            if not queryset.is_active:
                raise forms.ValidationError(
                    ("Usuario deshabilitado, consulte con el administrador."),
                    code='invalid',
                )

            if user is None:
                raise forms.ValidationError(
                    ("Usuario y Contraseña no coiciden."),
                    code='invalid',
                )

        except UserModel.DoesNotExist:
            raise forms.ValidationError(
                ("Usuario y Contraseña no coiciden."),
                code='invalid',
            )
        return super(UserLoginForm, self).clean(*args, **kwargs)
