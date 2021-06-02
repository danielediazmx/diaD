from django.shortcuts import render
from django.views import View
from tablib import Dataset

from Registro.models import Registro
from excel_importer.resources import RegistroResource


class ExcelImporter(View):
    def get(self, request):
        return render(request, 'excel_importer/index.html')

    def post(self, request):
        persona_resource = RegistroResource()
        dataset = Dataset()
        nuevas_personas = request.FILES['xlsfile']
        imported_data = dataset.load(nuevas_personas.read(), format="xlsx")
        result = persona_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            persona_resource.import_data(dataset, dry_run=False)
        else:
            print('has errors', result.row_errors())

        return render(request, 'excel_importer/index.html')
