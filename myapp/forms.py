from django import forms
from .models import Doe_computer,Doe_copier,Doe_printer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Doe_computer
        fields = '__all__'
        labels={ 'cpu':'CPU', 'hdd':'HDD' , 'ip':'IP'}


class CopierForm(forms.ModelForm):
    class Meta:
        model = Doe_copier
        fields = '__all__'
        labels = {'brand_name': 'Model Name', 'copier_ip': 'IP', 'copier_place': 'Location','copier_company':'Company','copier_company_phone':'Contact Number','copier_driver':'Driver'}

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Doe_printer
        fields = '__all__'