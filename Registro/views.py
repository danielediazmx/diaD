import random

from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from Registro.models import Registro


class RegistrosView(View):
    def get(self, request):
        user = request.user

        registros_list = Registro.objects.filter(invitado_por=user.first_name).all()
        page = request.GET.get('page', 1)
        paginator = Paginator(registros_list, 25)

        try:
            registros = paginator.page(page)
        except PageNotAnInteger:
            registros = paginator.page(1)
        except EmptyPage:
            registros = paginator.page(paginator.num_pages)

        index = registros.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
        page_range = list(paginator.page_range)[start_index:end_index]

        return render(request, 'Registro/index.html', {'registros': registros, 'page_range': page_range})


class RegistroMarcarVotoView(View):
    def get(self, request, id, ya_voto):
        registro: Registro = Registro.objects.filter(pk=id).first() or None
        if registro:
            registro.ya_voto = ya_voto
            registro.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/registros'))


def registro_create_users(request):
    registros = Registro.objects.all()

    def generateUsername(registro):
        username = str(str(registro.invitado_por).lower().split(" ")[0]) + str(random.randint(1000, 10000))
        user = User.objects.filter(username=username).first() or None

        if user:
            return generateUsername(registro)

        return username

    for registro in registros:
        user = User.objects.filter(first_name=registro.invitado_por).first() or None
        if not user:
            username = generateUsername(registro)
            email = username + "@gmail.com"
            password = username + ".01"

            User.objects.create_user(username, email, password, first_name=registro.invitado_por)

    return HttpResponse("HMM")
