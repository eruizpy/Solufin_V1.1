from django.contrib.auth import (
    get_user_model,
    authenticate,
    login,
    logout,
)
from django.shortcuts import render, redirect
from Solufin.forms import UserLoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
UserModel = get_user_model()


def acceso(request):
    template_name = 'login/login.html'
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(form.cleaned_data)
            try:
                myuser = UserModel.objects.get(email=email)
                user = authenticate(
                    username=myuser.username,
                    password=password,
                )
                if user is None:
                    return redirect('login')
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponseRedirect('inactivo_user')
            except UserModel.DoesNotExist:
                return None
        else:
            print(form.errors)
    return render(
        request,
        template_name,
        {
            'form': form,
        }
    )


@login_required(login_url="login")
def index(request):
    template_name = 'index/index.html'
    return render(
        request,
        template_name,
    )


def inactivo_user(request):
    template_name = 'index/inactivo_user.html'
    return render(
        request,
        template_name
    )


def logout_view(request):
    logout(request)
    return redirect('login')
