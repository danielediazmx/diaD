from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
from Registro.models import Registro


def index(request):
    user = request.user

    total_registros = Registro.objects.filter(invitado_por=user.first_name).count()
    ya_votaron = Registro.objects.filter(invitado_por=user.first_name, ya_voto=True).count()
    no_han_votado = Registro.objects.filter(invitado_por=user.first_name, ya_voto=False).count()
    eficiencia = round(ya_votaron * 100 / total_registros if ya_votaron > 0 else 0, 2)

    return render(request, 'dashboard.html',
                  {'total_registros': total_registros, 'ya_votaron': ya_votaron,
                   'no_han_votado': no_han_votado, 'eficiencia': eficiencia})


def dashboard_two(request):
    user: User = request.user

    coordinacion = request.GET.get('coordinacion', False)
    coordinaciones = Registro.objects.values("coordinacion").annotate(coordinacion_count=Sum("coordinacion"))

    registrosBase = Registro.objects

    if coordinacion:
        registrosBase = registrosBase.filter(coordinacion=coordinacion)

    total_registros = registrosBase.count()
    ya_votaron = registrosBase.filter(ya_voto=True).count()
    no_han_votado = registrosBase.filter(ya_voto=False).count()
    eficiencia = round(ya_votaron * 100 / total_registros if ya_votaron > 0 else 0, 2)

    if not user.is_superuser:
        total_registros = Registro.objects.filter(invitado_por=user.first_name).count()
        ya_votaron = Registro.objects.filter(invitado_por=user.first_name, ya_voto=True).count()
        no_han_votado = Registro.objects.filter(invitado_por=user.first_name, ya_voto=False).count()
        eficiencia = round(ya_votaron * 100 / total_registros if ya_votaron > 0 else 0, 2)

    return render(request, 'dashboard_two.html',
                  {
                      'total_registros': total_registros, 'ya_votaron': ya_votaron,
                      'no_han_votado': no_han_votado, 'eficiencia': eficiencia,
                      'coordinaciones': coordinaciones, 'coordinacionSelected': coordinacion
                  })


def users_list(request):
    users = User.objects.all()
    return render(request, 'usuarios.html', {'users': users})
