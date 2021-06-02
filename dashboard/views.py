from django.shortcuts import render

# Create your views here.
from Registro.models import Registro


def index(request):
    total_registros = Registro.objects.count()
    ya_votaron = Registro.objects.filter(ya_voto=True).count()
    no_han_votado = Registro.objects.filter(ya_voto=False).count()
    eficiencia = round(ya_votaron * 100 / total_registros if ya_votaron > 0 else 0, 2)

    return render(request, 'dashboard.html',
                  {'total_registros': total_registros, 'ya_votaron': ya_votaron,
                   'no_han_votado': no_han_votado, 'eficiencia': eficiencia})
