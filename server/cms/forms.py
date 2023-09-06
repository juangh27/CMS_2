from django import forms
from django.core.validators import DecimalValidator
from .models import MedicalEquipments, MedicalEquipmentDetails


class MedicalEquipmentForm(forms.ModelForm):
    class Meta:
        model = MedicalEquipments
        exclude = ['group']
        fields = '__all__'  # Include all fields from the model
        # You can also specify the fields explicitly like:
        # fields = ['serial_number', 'equipment_type', 'manufacturer', 'model', 'calibration_date', 'last_service_date', 'is_active']
        
        widgets = {
            'servicio_ult': forms.DateInput(attrs={'type': 'date'}),
            'servicio_prox': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
        
    def as_two_column(self):
        # Add 'row' class to the form
        self.form_class = 'row'

        # Add 'col-sm-6' class to each field wrapper
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'col-sm-6'

        return self
class MedicalDetailsEquipmentForm(forms.ModelForm):
    equipo = forms.ModelChoiceField(queryset=MedicalEquipments.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = MedicalEquipmentDetails
        fields = '__all__'  # Include all fields from the model
        # You can also specify the fields explicitly like:
        # fields = ['serial_number', 'equipment_type', 'manufacturer', 'model', 'calibration_date', 'last_service_date', 'is_active']
        exclude = ('equipo',)
        widgets = {
            'instalacion_fecha': forms.DateInput(attrs={'type': 'date'}),
            'ultima_actualizacion': forms.DateInput(attrs={'type': 'date'}),
            'adquisicion': forms.DateInput(attrs={'type': 'date'}),
            'ultimo_mprev': forms.DateInput(attrs={'type': 'date'}),
            'proximo_mprev': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['instalacion_fecha'].required = False
        self.fields['ultimo_mprev'].required = False
        self.fields['proximo_mprev'].required = False
        self.fields['ultima_actualizacion'].required = False
        self.fields['adquisicion'].required = False
        self.fields['precio_compra'].required = False
        equipment_id = kwargs.pop('equipment_id', None)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        if equipment_id:
            self.initial['equipo'] = equipment_id
            
    def as_two_column(self):
        # Add 'row' class to the form
        self.form_class = 'row'

        # Add 'col-sm-6' class to each field wrapper
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'col-sm-6'

        return self