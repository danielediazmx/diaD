"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from Registro.views import RegistrosView, RegistroMarcarVotoView, registro_create_users
from dashboard.views import index, users_list, dashboard_two
from excel_importer.views import ExcelImporter

urlpatterns = [
    path('', login_required(dashboard_two)),
    path('dashboard-two/', login_required(dashboard_two)),
    path('users-list/', users_list),
    path('accounts/', include('django.contrib.auth.urls')),
    path('excel-importer/', login_required(ExcelImporter.as_view())),
    path('registros/', login_required(RegistrosView.as_view()), name='registros'),
    path('registros/marcar-voto/<int:id>/<int:ya_voto>/', login_required(RegistroMarcarVotoView.as_view()), name='registros_marcar_voto'),
    path('registros/create-users/', login_required(registro_create_users), name='registros_create_users'),
    path('admin/', admin.site.urls),
]
