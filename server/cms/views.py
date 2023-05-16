from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings 
from cms.models import MenuSubItem2
from django.db import connection
from django.db import reset_queries

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

def sidebar(request):
    return render(request, 'cms/sidebar.html')


def test_templates(request):
    return render(request, 'cms/test_templates.html')

def test_nav(request):
    return render(request, 'cms/test_nav.html')

def test_body(request):
    return render(request, 'cms/test_body.html')

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