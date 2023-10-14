from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.conf import settings 
from django.db import connection, reset_queries
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from cms.serializers import UserSerializer, GroupSerializer
from cms.models import MenuSubItem2,MedicalEquipments ,User, MedicalEquipmentDetails, Room
from .forms import MedicalEquipmentForm, MedicalDetailsEquipmentForm
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth import authenticate, login,logout

def user_is_authenticated(user):
    return user.is_authenticated


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cms:dashboard')  # Replace 'home' with the URL name of your home page
        else:
            # Authentication failed, show error message
            error_message = 'Invalid username or password.'
            return render(request, 'cms/login.html', {'error_message': error_message})
    else:
        return render(request, 'cms/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('cms:login')


def edit_equipment(request, equipment_id=None):
    if equipment_id:
        equipment = get_object_or_404(MedicalEquipments, id=equipment_id)
    else:
        equipment = None
    

    if request.method == 'POST':
        group = request.user.groups.first()
        form = MedicalEquipmentForm(request.POST, instance=equipment)
        
        print(group)
        print(form)
        if form.is_valid():
            instance = form.save(commit=False)
            print('test intance')

            # Add the excluded field value to the instance
            group_id = group.id
            print(group_id)
            print(instance.group_id)
            instance.group_id = group_id
            print(instance.group_id)
            instance.save()
            return JsonResponse({'success': True})  # Return success response as JSON
        else:
            return JsonResponse({'success': False, 'errors': form.errors})  # Return form errors as JSON
    else:
        form = MedicalEquipmentForm(instance=equipment)

    return render(request, 'cms/modals/equipment_modal.html', {'form': form, 'equipment': equipment})

def equipment_details(request, equipment_id=None):
    equipment = get_object_or_404(MedicalEquipments, id=equipment_id)
    details = MedicalEquipmentDetails.objects.filter(equipo=equipment).first()

    if request.method == 'POST':
        form = MedicalDetailsEquipmentForm(request.POST, instance=details)
        if form.is_valid():
            details = form.save(commit=False)
            details.equipo = equipment
            print(equipment)
            print('equipment')
            details.save()
            return JsonResponse({'success': True})  # Return success response as JSON
        else:
            return JsonResponse({'success': False, 'errors': form.errors})  # Return form errors as JSON
    else:
        form = MedicalDetailsEquipmentForm(instance=details, initial={'equipo': equipment_id})

    return render(request, 'cms/modals/equipment_details_modal.html', {'form': form, 'equipment': equipment})


def get_equipment_details(request, equipment_id):
    try:
        details = MedicalEquipmentDetails.objects.get(equipo_id=equipment_id)
        data = {
            'instalacion_fecha': details.instalacion_fecha,
            'anios_operando': details.anios_operando,
            'ultima_actualizacion': details.ultima_actualizacion,
            'estatus': details.estatus,
            'ubicacion': details.ubicacion,
            'sub_ubicacion': details.sub_ubicacion,
            'pertenencia': details.pertenencia,
            'duenio': details.duenio,
            'vendido_por': details.vendido_por,
            'adquisicion': details.adquisicion,
            'precio_compra': str(details.precio_compra),
            'divisas': details.divisas,
            'provedor': details.provedor,
            'frecuencia_mprev': details.frecuencia_mprev,
            'ultimo_mprev': details.ultimo_mprev,
            'proximo_mprev': details.proximo_mprev,
            'riesgo': details.riesgo,
            'cricticidad': details.cricticidad,
            'garantia': details.garantia,
            'accesorios': details.accesorios,
        }
        return JsonResponse(data)
    except MedicalEquipmentDetails.DoesNotExist:
        return JsonResponse({'error': 'Equipment details not found'})
    
   
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class MedicalEquipmentJson(BaseDatatableView):
    model = MedicalEquipments
    columns = ['serial_number', 'equipment_type', 'manufacturer', 'model', 'calibration_date', 'last_service_date', 'is_active']

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_initial_queryset(self):
        return self.model.objects.all()

    def prepare_results(self, qs):
        data = []
        user_group = self.request.user.groups.first()  # Get the first group the user belongs to
        if user_group:
            qs = qs.filter(group=user_group)
        for item in qs:
            edit_button = f'<a href="#" class="btn btn-outline-info" data-equipment-id="{item.pk}" id="edit-btn">Editar</a>'
            delete_button = f'<a href="#" class="btn btn-outline-danger" data-equipment-id="{item.pk}" id="delete-btn">Borrar</a>'
            data.append({
            'id': item.pk,
            'equipo': item.equipo,
            'marca': item.marca,
            'modelo': item.modelo,
            'no_serie': item.no_serie,
            'servicio_ult': item.servicio_ult.strftime('%Y-%m-%d'),
            'servicio_prox': item.servicio_prox.strftime('%Y-%m-%d'),
            'estado': item.estado,
            'area': item.area,
            'subarea': item.subarea,
            'encargado': item.encargado,
            'group': item.group.name,  # Assuming 'name' is the field to display for the Group model
            'actions': f'{edit_button} | {delete_button}'
            })
        return data
# class MedicalEquipmentJson(BaseDatatableView):
#     model = MedicalEquipments
#     columns = ['serial_number', 'equipment_type', 'manufacturer', 'model', 'calibration_date', 'last_service_date', 'is_active']

#     @csrf_exempt
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def get_initial_queryset(self):
#         return self.model.objects.all()

#     def prepare_results(self, qs):
#         data = []
#         for item in qs:
#             edit_button = f'<a href="#" class="btn btn-outline-info" data-equipment-id="{item.pk}" id="edit-btn">Editar</a>'
#             delete_button = f'<a href="#" class="btn btn-outline-danger" data-equipment-id="{item.pk}" id="delete-btn">Borrar</a>'
#             data.append({
#             'id': item.id,
#             'serial_number': item.serial_number,
#             'equipment_type': item.get_equipment_type_display(),
#             'manufacturer': item.manufacturer,
#             'model': item.model,
#             'calibration_date': item.calibration_date.strftime('%Y-%m-%d'),
#             'last_service_date': item.last_service_date.strftime('%Y-%m-%d'),
#             'is_active': str(item.is_active),
#             'actions' : f'{edit_button} | {delete_button}'
#             })
#         return data

def menu_items():
    navbar = MenuSubItem2.objects.filter(parent=None).prefetch_related('parent__menusubitem2_set').order_by('id')
    return navbar
@user_passes_test(user_is_authenticated, login_url='/login/') 
def dashboard(request, **kwargs):
    # User is logged in
    user = request.user

    # Get the groups the user belongs to
    groups = user.groups.all()
    if not groups:
    # No groups found, it is empty
        context = {'menu_items': menu_items, 'page_title': 'Dashboard', 'page_subtitle': 'No esta logeado',"user":user}
    else:
    # Groups found, iterate over them or perform other operations
        for group in groups:
            group_name = group.name
        context = {'menu_items': menu_items, 'page_title': 'Dashboard', 'page_subtitle': 'Aqui puede ver su informacion general',"user":user, 'group': group_name}
        # ... other group attributes
    # Iterate over the groups and access their attributes

    
    return render(request, 'cms/child_dashboard.html', context=context)
@user_passes_test(user_is_authenticated, login_url='/login/') 
def inventario(request, **kwargs):
    context = {'menu_items': menu_items, 'page_title': 'Inventario', 'page_subtitle': 'Estos son los equipos con los que cuenta'}
    return render(request, 'cms/child_inventario.html', context=context)
@user_passes_test(user_is_authenticated, login_url='/login/') 
def detalles(request, **kwargs):
    context = {'menu_items': menu_items, 'page_title': 'Detalles', 'page_subtitle': 'Especificaciones de los equipos con los que cuenta'}
    return render(request, 'cms/child_detalles.html', context=context)
@user_passes_test(user_is_authenticated, login_url='/login/') 
def provedores(request, **kwargs):
    context = {'menu_items': menu_items, 'page_title': 'Provedores', 'page_subtitle': 'Subtitulo provedores'}
    return render(request, 'cms/child_provedores.html', context=context)
@user_passes_test(user_is_authenticated, login_url='/login/') 
def servicios(request, **kwargs):
    context = {'menu_items': menu_items, 'page_title': 'Servicios', 'page_subtitle': 'This is an example page'}
    return render(request, 'cms/child_servicios.html', context=context)
@user_passes_test(user_is_authenticated, login_url='/login/') 
def calendarios(request, **kwargs):
    context = {'menu_items': menu_items, 'page_title': 'Calendarios', 'page_subtitle': ''}
    return render(request, 'cms/child_calendarios.html', context=context)
@user_passes_test(user_is_authenticated, login_url='/login/') 
def cuenta(request, **kwargs):
    context = {'menu_items': menu_items, 'page_title': 'Cuenta', 'page_subtitle': 'Configuracion de la cuenta'}
    return render(request, 'cms/child_cuenta.html', context=context)
def chat(request, **kwargs):
    rooms = Room.objects.filter(name__in=["help", "questions", "urgent"])
    context = {'menu_items': menu_items, 'page_title': 'Chat', 'page_subtitle': 'Mensajes a soporte tecnico','rooms': rooms}
    return render(request, 'cms/child_chat.html',context=context)

def room_view(request, room_name, **kwargs):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    context = {'menu_items': menu_items, 'page_title': 'Cuenta', 'page_subtitle': 'Configuracion de la cuenta','room': chat_room}
    return render(request, 'cms/child_room.html', context=context)

def register_delete(request, equipment_id=0):
    print(request)
    print(equipment_id)
    my_model = get_object_or_404(MedicalEquipments, id=equipment_id)
    my_model.delete()
    return JsonResponse({'success': True})
    