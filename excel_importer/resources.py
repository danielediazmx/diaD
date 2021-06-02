from import_export import resources
from Registro.models import Registro


class RegistroResource(resources.ModelResource):
    class Meta:
        model = Registro
