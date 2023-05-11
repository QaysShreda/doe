from django import forms
from .models import *




class DateInput(forms.DateInput):
    input_type = 'date'


class ComputerForm(forms.ModelForm):
    class Meta:
        model = Doe_computer
        fields = '__all__'
        labels={ 'cpu':'CPU', 'hdd':'HDD' ,'hdd_type':'HDD Type', 'ip':'IP','ram_type':'Ram Type','serial':'Serial Number','anti_virus':'Anti Virus','expiry_date':'Expiry Date'}
        widgets = {
            'expiry_date': DateInput(),
        }

class CopierForm(forms.ModelForm):
    class Meta:
        model = Doe_copier
        fields = '__all__'
        labels = {'brand_name': 'Model Name', 'ip': 'IP', 'place': 'Location','company':'Company','company_phone':'Contact Number','driver':'Driver'}

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Doe_printer
        fields = '__all__'

class ProjectorForm(forms.ModelForm):
    class Meta:
        model = Doe_projector
        fields = '__all__'

class FiberForm(forms.ModelForm):
    class Meta:
        model = Doe_Fiber
        fields = '__all__'

class IPForm(forms.ModelForm):
    class Meta:
        model = Common_Ip
        fields = '__all__'

class WifiForm(forms.ModelForm):
    class Meta:
        model = Doe_Wifi
        fields = '__all__'
        labels={'router':'Router Model','ip':'IP address','lan':'Internal Lan','ssid':'SSID'}

class School_form(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
        labels={ 'school_id':'National number','name':'School Name ar','name_en':'School Name en','l_level':'Lower Level','u_level':'Upper Level','st_number':'Student number','phone_number':'Phone','mobile':'Principal mobile','science':'علمي' ,'literary':'أدبي','commercial':'تجاري' ,'industrial':'صناعي'}

class School_lab_form(forms.ModelForm):
    class Meta:
        model = School_lab
        fields = '__all__'
        labels={'lab_id':'Lab id','network':'Network','area':'Area (m2)','internet_connection':'Internet Connections:','school':'Select School Name :'}

class School_Computer_Form(forms.ModelForm):
    class Meta:
        model = School_computer
        fields = '__all__'

class School_Network_Form(forms.ModelForm):
    class Meta:
        model = School_Network
        fields = '__all__'
        labels={'internet':'Yes','wifi':'Yes','speed_download':'Download Speed','speed_upload':'Upload Speed','router':'Router Brand','lan':'Yes','port':'Number of Ports','ap_number':'AP Number'}