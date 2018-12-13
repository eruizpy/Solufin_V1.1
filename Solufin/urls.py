"""Solufin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Solufin.views import acceso, index, inactivo_user, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('inactivo/', inactivo_user, name='inactivo'),
    path('', include('apps.cliente.urls')),
    path('propuesta/', include('apps.propuesta.urls')),
    path('login/', acceso, name='login'),
    path(
        'logout/',
        logout_view,
        name='logout',
    ),
]
