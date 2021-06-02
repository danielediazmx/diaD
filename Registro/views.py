from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import View

from Registro.models import Registro


class RegistrosView(View):
    def get(self, request):
        registros_list = Registro.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(registros_list, 10)

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
