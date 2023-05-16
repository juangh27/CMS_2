from django.urls import path


from . import views
from django.views.generic import TemplateView

app_name = 'cms'
urlpatterns = [
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
    path('sidebar/', views.sidebar, name='sidebar'),
    path('templates/', views.test_templates, name='templates'),
    path('test_nav/', views.test_nav, name='test_nav'),
    path('test_body/', views.test_body, name='test_body'),
    path('', views.dashboard, name='dashboard'),
    path('inventario/', views.inventario, name='inventario'),
    path('provedores/', views.provedores, name='provedores'),
    path('servicios/', views.servicios, name='servicios'),
    path('calendarios/', views.calendarios, name='calendarios'),
    path('cuenta/', views.cuenta, name='cuenta'),
    
]
