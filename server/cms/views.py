from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings 
from cms.models import MenuSubItem2,MedicalEquipment
from django.db import connection
from django.db import reset_queries
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from django.views.generic.base import TemplateView


def test(request):
    template = loader.get_template('cms/test.html')
    context = {
        'aves': ['Quetzal', 'Aguila Arpia', 'Emu', 'Colibri']
    }
    return HttpResponse(template.render(context, request))

# Ejemplo de una pagina simple

def test2(request):
    return render(request, 'cms/test2.html')


def test_copy(request):
    return render(request, 'cms/test_copy.html')

def sidebar(request):
    return render(request, 'cms/sidebar.html')


def test_templates(request):
    return render(request, 'cms/test_templates.html')

def test_nav(request):
    return render(request, 'cms/test_nav.html')

def test_body(request):
    return render(request, 'cms/test_body.html')

class MedicalEquipmentJson(BaseDatatableView):
    model = MedicalEquipment
    columns = ['serial_number', 'equipment_type', 'manufacturer', 'model', 'calibration_date', 'last_service_date', 'is_active']

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        return self.model.objects.all()

    def prepare_results(self, qs):
        data = []
        for item in qs:
            edit_button = f'<a href="#" class="btn btn-outline-info" data-equipment-id="{item.pk}" id="edit-btn">Editar</a>'
            delete_button = f'<a href="#" class="btn btn-outline-danger" data-equipment-id="{item.pk}" id="delete-btn">Borrar</a>'
            data.append({
            'id': item.id,
            'serial_number': item.serial_number,
            'equipment_type': item.get_equipment_type_display(),
            'manufacturer': item.manufacturer,
            'model': item.model,
            'calibration_date': item.calibration_date.strftime('%Y-%m-%d'),
            'last_service_date': item.last_service_date.strftime('%Y-%m-%d'),
            'is_active': str(item.is_active),
            'actions' : f'{edit_button} | {delete_button}'
            })
        return data

def menu_items():
    navbar = MenuSubItem2.objects.filter(parent=None).prefetch_related('parent__menusubitem2_set').order_by('id')
    return navbar

def dashboard(request, **kwargs):
    context = {'menu_items': menu_items, 'page_title': 'Dashboard', 'page_subtitle': 'Aqui puede ver su informacion general'}
    return render(request, 'cms/child_dashboard.html', context=context)

def inventario(request, **kwargs):
    context = {'menu_items': menu_items, 'page_title': 'Inventario', 'page_subtitle': 'Estos son los equipos con los que cuenta'}
    return render(request, 'cms/child_inventario.html', context=context)

def provedores(request, **kwargs):
    context = {'menu_items': menu_items, 'page_title': 'Provedores', 'page_subtitle': 'Subtitulo provedores'}
    return render(request, 'cms/child_provedores.html', context=context)

def servicios(request, **kwargs):
    context = {'menu_items': menu_items, 'page_title': 'Servicios', 'page_subtitle': 'This is an example page'}
    return render(request, 'cms/child_servicios.html', context=context)

def calendarios(request, **kwargs):
    context = {'menu_items': menu_items, 'page_title': 'Calendarios', 'page_subtitle': ''}
    return render(request, 'cms/child_calendarios.html', context=context)

def cuenta(request, **kwargs):
    context = {'menu_items': menu_items, 'page_title': 'Cuenta', 'page_subtitle': 'Configuracion de la cuenta'}
    return render(request, 'cms/child_cuenta.html', context=context)