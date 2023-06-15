from django.urls import path


from . import views
from django.views.generic import TemplateView
from .views import MedicalEquipmentJson

app_name = 'cms'
urlpatterns = [
    # path('test/', views.test, name='test'),
    # path('test_copy/', views.test_copy, name='test_copy'),
    # path('test2/', views.test2, name='test2'),
    # path('sidebar/', views.sidebar, name='sidebar'),
    # path('templates/', views.test_templates, name='templates'),
    # path('test_nav/', views.test_nav, name='test_nav'),
    # path('test_body/', views.test_body, name='test_body'),
    path('', views.dashboard, name='dashboard'),
    path('inventario/', views.inventario, name='inventario'),
    path('detalles/', views.detalles, name='detalles'),
    path('provedores/', views.provedores, name='provedores'),
    path('servicios/', views.servicios, name='servicios'),
    path('calendarios/', views.calendarios, name='calendarios'),
    path('cuenta/', views.cuenta, name='cuenta'),
    path('equipment-data/', MedicalEquipmentJson.as_view(), name='equipment_data'),
    path('login/', views.login_view, name='login'),
    path('equipment_details_view/<int:equipment_id>', views.get_equipment_details, name='equipment_details_view'),
    path('equipment_details_view/', views.get_equipment_details, name='equipment_details_view'),
    path('equipment_details_modal/', views.equipment_details, name='equipment_details'),
    path('equipment_details_modal/<int:equipment_id>', views.equipment_details, name='equipment_details'),
    path('edit-equipment/<int:equipment_id>/', views.edit_equipment, name='edit_equipment'),
    path('edit-equipment/', views.edit_equipment, name='edit_equipment'),
    path('logout/', views.logout_view, name='logout'),

    
]
