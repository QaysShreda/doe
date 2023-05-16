from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
<<<<<<< HEAD
from .forms import *
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required




=======
from .forms import ComputerForm,CopierForm,PrinterForm,ProjectorForm,FiberForm,IPForm,WifiForm,School_lab_form,School_form,School_Computer_Form
from .models import Doe_computer,Doe_copier,Doe_printer,Doe_projector,Doe_Fiber,Doe_Wifi,Common_Ip,School_lab,School,School_computer
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
>>>>>>> ead5f86ecc5368730894716184880ac4d5d84c5c
# Create your views here.


@login_required(login_url='login')
def index(request):

    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/index')
        else:
            messages.info(request,'Enter valid user name or password !!')
            return redirect('/')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        user = User.objects.create_user(username= user_name, password = password1, email=email,first_name=first_name,last_name=last_name)
        if password1 == password2:
            if User.objects.filter(username = user_name).exists():
                print('User Taken')
            else:
                user.save();
                print('success')

        else:
            print('Password not matching...')
        return redirect('login')
            
        
    else:
        return render(request,'register.html')

@login_required(login_url='login')
def school(request):
    return render(request,'school.html')

@login_required(login_url='login')
def doe(request):
    return render(request,'doe.html')

@login_required(login_url='login')
def doe_computer(request):
    context = {'doe_computer': Doe_computer.objects.all()}
    return render(request,'doe_computer.html',context)


@login_required(login_url='login')
def computer_form(request,id =0):
    if request.method == "GET":
        if id == 0:
            form = ComputerForm()
        else:
            computer = Doe_computer.objects.get(pk=id)
            form = ComputerForm(instance=computer)
        return render(request,'computer_form.html',{'form':form})
    else:
        if id==0:
            form = ComputerForm(request.POST)
        else:
            computer = Doe_computer.objects.get(pk=id)
            form = ComputerForm(request.POST,instance=computer)
        if form.is_valid():
            form.save()
        return redirect('/doe_computer')

def computer_delete(request, id):
    computer = Doe_computer.objects.get(pk=id)
    computer.delete()
    return redirect('/doe_computer')

# DOE Copier
def doe_copier(request):
    context = {'doe_copier': Doe_copier.objects.all()}
    return render(request,'doe_copier.html',context)

def doe_copier_form(request,id=0):
    if request.method == "GET":
        if id ==0:
            form = CopierForm()
        else:
            copier = Doe_copier.objects.get(pk=id)
            form = CopierForm(instance=copier)
        return render(request,'doe_copier_form.html', {'form':form})
    else:
        if id ==0:
            form = CopierForm(request.POST)
        else:
            copier = Doe_copier.objects.get(pk=id)
            form = CopierForm(request.POST, instance=copier)
        if form.is_valid():
             form.save()
        return redirect('/doe_copier')

def doe_copier_delete(request, id):
    copier = Doe_copier.objects.get(pk=id)
    copier.delete()
    return redirect('/doe_copier')


#DOE Printer
@login_required(login_url='login')
def doe_printer(request):
    context = {'doe_printer':Doe_printer.objects.all()}
    return render(request,'doe_printer.html',context)


def doe_printer_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = PrinterForm()
        else:
            printer = Doe_printer.objects.get(pk=id)
            form = PrinterForm(instance=printer)
        return render(request,'doe_printer_form.html',{'form':form})
    else:
        if id == 0:
            form = PrinterForm(request.POST)
        else:
            printer = Doe_printer.objects.get(pk=1)
            form = PrinterForm(request.POST,'doe_printer_form',instance=printer)
        if form.is_valid():
            form.save()
        return redirect('/doe_printer')   
    
def doe_printer_delete(request,id):
    printer = Doe_printer.objects.get(pk=id)
    printer.delete()
    return redirect('/doe_printer')


#DOE PROJECTOR
def doe_projector(request):
    context = {'doe_projector':Doe_projector.objects.all}
    return render(request,'doe_projector.html',context)

def doe_projector_form(request,id=0):
    if request.method == 'GET':
        if id ==0 :
            form = ProjectorForm()
        else:
            projector = Doe_projector.objects.get(pk=id)
            form = ProjectorForm(instance=projector)
        return render(request, 'doe_projector_form.html', {'form': form})
    else:
        if id == 0:
            form = ProjectorForm(request.POST)
        else:
            projector = Doe_projector.objects.get(pk=id)
            form = ProjectorForm(request.POST,'doe_projector_form',instance=projector)

        if form.is_valid():
            form.save()
        return redirect('doe_projector')
    
def doe_projector_delete(request,id):
    projector = Doe_projector.objects.get(pk=id)
    projector.delete()
    return redirect('/doe_projector')
<<<<<<< HEAD


#NETWORK

def doe_network(request):
    context = {'ip':Common_Ip.objects.all(),'fiber': Doe_Fiber.objects.all(),'wifi':Doe_Wifi.objects.all()}
    return render(request,'doe_network.html',context )


# Fiber
def doe_fiber_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = FiberForm()
        else:
            fiber = Doe_Fiber.objects.get(pk=id)
            form = FiberForm(instance=fiber)
        return render(request,'doe_fiber_form.html',{'form':form})
    else:
        if id == 0:
            form = FiberForm(request.POST)
        else:
            fiber = Doe_Fiber.objects.get(pk=id)
            form = FiberForm(request.POST,'doe_fiber_form',instance=fiber)
        if form.is_valid():
            form.save()
            return redirect('doe_network')


def doe_fiber_delete(request,id):
    fiber = Doe_Fiber.objects.get(pk=id)
    fiber.delete()
    return redirect('/doe_network')

#IP
def doe_ip_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = IPForm()
        else:
            IP = Common_Ip.objects.get(pk=id)
            form = IPForm(instance=IP)
        return render(request,'doe_ip_form.html',{'form':form})
    else:
        if id == 0:
            form = IPForm(request.POST)
        else:
            IP = Common_Ip.objects.get(pk=id)
            form = IPForm(request.POST,'doe_ip_form',instance=IP)
        if form.is_valid():
            form.save()
            return redirect('doe_network')


def doe_ip_delete(request,id):
    IP = Common_Ip.objects.get(pk=id)
    IP.delete()
    return redirect('/doe_network')

# Wifi

def doe_wifi_form(request,id=0):
    if request.method == 'GET':
        if id == 0 :
            form = WifiForm()
        else:
            wifi = Doe_Wifi.objects.get(pk=id)
            form = WifiForm(instance=wifi)
        return render(request,'doe_wifi_form.html',{'form':form})
    else:
        if id == 0:
            form = WifiForm(request.POST)
        else:
            wifi = Doe_Wifi.objects.get(pk=id)
            form = WifiForm(request.POST,'doe_wifi_form',instance=wifi)
        if form.is_valid():
            form.save()
            return redirect('/doe_network')

def doe_wifi_delete(request,id):
    wifi = Doe_Wifi.objects.get(pk=id)
    wifi.delete()
    return redirect('/doe_network')

# School
def school_info(request):
    school = School.objects.all()
    return render(request,'school_info.html',{'school':school})


def school_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = School_form
        else:
            school = School.objects.get(pk=id)
            form = School_form(instance=school)
        return render(request, 'school_form.html', {'form': form})
    else:
        if id ==0 :
            form = School_form(request.POST)
        else:
            school = School.objects.get(pk=id)
            form = School_form(request.POST,'school_form',instance=school)
        if form.is_valid():
            form.save()
            return redirect('school_info')
def school_delete(request,id =0):
    if id != 0:
        school = School.objects.get(pk=id)
        school.delete()
        return redirect('school_info')


# School Lab
def school_lab(requiest):
    context = {'school_lab':School_lab.objects.all()}
    return render(requiest,'school_lab.html',context)

def school_lab_form(request,id=0):
    if request.method == "GET":
        if id ==0:
            form = School_lab_form()
        else:
            school_lab = School_lab.objects.get(id = id )
            form = School_lab_form(instance=school_lab)
        return render(request,'school_lab_form.html', {'form':form})
    else:
        if id ==0:
            form = School_lab_form(request.POST)
        else:
            school_lab = School_lab.objects.get(id=id)
            form = School_lab_form(request.POST, instance=school_lab)
        if form.is_valid():
             form.save()
        return redirect('/school_lab')

def school_lab_delete(request,id=0):
    if id!=0:
        school_lab = School_lab.objects.get(pk=id)
        school_lab.delete()
    return redirect('/school_lab')



def school_lab_computers(request,id=0):
    if id == 0 :
        return render(request, 'school_lab.html')
    else:
        lab = School_lab.objects.get(id = id)
        computer = School_computer.objects.filter(lab = lab)
    return render(request,'school_lab_computers.html',{'computer':computer,'lab':lab})


def school_computer_form(request,lab=0,id=0):
    lab = School_lab.objects.get(id = lab)
    if request.method == "GET":
        if id==0:
            form = School_Computer_Form()
        else:
            computer = School_computer.objects.get(id=id)
            form = School_Computer_Form(instance=computer)

        return render(request, 'school_computer_form.html', {'form': form,'lab':lab})
    else:
        if id == 0 :
            form = School_Computer_Form(request.POST)
        else:
            computer = School_computer.objects.get(pk=id)
            form = School_Computer_Form(request.POST,instance=computer)
        x = form['lab'].value()
        form.save()
        return school_lab_computers(request,x)

def school_computer_delete(request,id=0):
    if id !=0:
        computer = School_computer.objects.get(pk=id)
        my_lab = computer.lab
        x = my_lab.id
        computer.delete()
    return school_lab_computers(request,x)

def school_network(request):
    school_network = School_Network.objects.all()
    return render(request,'school_network.html',{'school_network':school_network})

def school_network_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = School_Network_Form()
        else:
            network = School_Network.objects.get(pk=id)
            form = School_Network_Form(instance=network)
        return render(request,'school_network_form.html',{'form':form})
    else:
        if id==0:
            form = School_Network_Form(request.POST)
        else:
            network = School_Network.objects.get(pk=id)
            form = School_Network_Form(request.POST,instance=network)
    if form.is_valid():
        form.save()      
    return redirect('school_network')
            
def school_network_delete(request,id=0):
    if id !=0:
       network = School_Network.objects.get(id=id)
       network.delete()
    return redirect('school_network')

def exportDoeComputer(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Doe_computers.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('computer')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Emp Name', 'Department', 'Brand' ,'CPU','Ram','Ram Type','HDD','Hdd_type','IP','Monitor','Serial','Anti Virus','Expired']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = Doe_computer.objects.all().values_list('employee_name','department','brand_name','cpu','ram','ram_type','hdd','hdd_type','ip','monitor','serial','anti_viruse','expiry_date')


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):

            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def exportSchoolInfo(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="SchoolInfo.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Schools')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id','Name','Name_en','L level','U level','Type','ST number','Phone','Location','Principal','Region','Mobile','Science','Literary','Commercial','Industrial']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = School.objects.all().values_list('school_id','name','name_en','l_level','u_level','type','st_number','phone_number','location','principal','region','mobile','science','literary','commercial','industrial')


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):

            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def exportSchoolLab(self):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="SchoolLab.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('School_Lab')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['school','Network','Area','Internal','Teacher','Load','Projector']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = School_lab.objects.all().values_list('school','network','area','internet_connection','teacher','teacher_load','projector')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):

            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def exportSchoolComputer(request,id =0):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="SchoolComputer.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('School_Computer')

    # Sheet header, first row
    row_num = 1

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Brand','CPU','Ram','Hdd','Internet','OS','Serial','Lab','School']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    if(id!=0):
        lab = School_lab.objects.get(id = id)

    rows = School_computer.objects.filter(lab = lab).values_list('brand','cpu','ram','hdd','internet','os','serial','lab','school')
    scholl = lab.school.name
    ws.write(0, 0, scholl, font_style)
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response




def exportDoeCopier(self):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="DoeCopier.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Doe_Copier')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Brand_name','IP','Location','Company','Company_phone','Driver']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = Doe_copier.objects.all().values_list('brand_name','ip','place','company','company_phone','driver')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):

            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def exportDoePrinter(self):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="DoePrinter.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Doe_Printer')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Model','Employee','Cartrigr_number','Driver']


    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = Doe_printer.objects.all().values_list('model_name','employee_name','Cartridge_number','driver')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):

            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



def exportSchoolNetwork(self):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="SchoolNetwork.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('School_Network')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['school Name','internet','Upload Speed','Download Speed','Source','Router','Wifi','AP number','AP brand','Coverage (100%)','Lan','Switch','Number Ports','School Id']


    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    schools = School.objects.all().values_list('school_id','name')
    font_style = xlwt.XFStyle()
    rows = School_Network.objects.all().values_list('internet','speed_upload','speed_download','source','router','wifi','ap_number','brand','coverage','lan','switch','port','school')
    for row in rows:
        row = list(row)
        row_num += 1
        for s in schools:
            if (s[0]==row[12]):
                  print(row[12]  )
                  row.insert(0, s[1])
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

=======
>>>>>>> ead5f86ecc5368730894716184880ac4d5d84c5c


#NETWORK

def doe_network(request):
    context = {'ip':Common_Ip.objects.all(),'fiber': Doe_Fiber.objects.all(),'wifi':Doe_Wifi.objects.all()}
    return render(request,'doe_network.html',context )


# Fiber
def doe_fiber_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = FiberForm()
        else:
            fiber = Doe_Fiber.objects.get(pk=id)
            form = FiberForm(instance=fiber)
        return render(request,'doe_fiber_form.html',{'form':form})
    else:
        if id == 0:
            form = FiberForm(request.POST)
        else:
            fiber = Doe_Fiber.objects.get(pk=id)
            form = FiberForm(request.POST,'doe_fiber_form',instance=fiber)
        if form.is_valid():
            form.save()
            return redirect('doe_network')


def doe_fiber_delete(request,id):
    fiber = Doe_Fiber.objects.get(pk=id)
    fiber.delete()
    return redirect('/doe_network')

#IP
def doe_ip_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = IPForm()
        else:
            IP = Common_Ip.objects.get(pk=id)
            form = IPForm(instance=IP)
        return render(request,'doe_ip_form.html',{'form':form})
    else:
        if id == 0:
            form = IPForm(request.POST)
        else:
            IP = Common_Ip.objects.get(pk=id)
            form = IPForm(request.POST,'doe_ip_form',instance=IP)
        if form.is_valid():
            form.save()
            return redirect('doe_network')


def doe_ip_delete(request,id):
    IP = Common_Ip.objects.get(pk=id)
    IP.delete()
    return redirect('/doe_network')

# Wifi

def doe_wifi_form(request,id=0):
    if request.method == 'GET':
        if id == 0 :
            form = WifiForm()
        else:
            wifi = Doe_Wifi.objects.get(pk=id)
            form = WifiForm(instance=wifi)
        return render(request,'doe_wifi_form.html',{'form':form})
    else:
        if id == 0:
            form = WifiForm(request.POST)
        else:
            wifi = Doe_Wifi.objects.get(pk=id)
            form = WifiForm(request.POST,'doe_wifi_form',instance=wifi)
        if form.is_valid():
            form.save()
            return redirect('/doe_network')

def doe_wifi_delete(request,id):
    wifi = Doe_Wifi.objects.get(pk=id)
    wifi.delete()
    return redirect('/doe_network')

# School
def school_info(request):
    school = School.objects.all()
    return render(request,'school_info.html',{'school':school})


def school_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = School_form
        else:
            school = School.objects.get(pk=id)
            form = School_form(instance=school)
        return render(request, 'school_form.html', {'form': form})
    else:
        if id ==0 :
            form = School_form(request.POST)
        else:
            school = School.objects.get(pk=id)
            form = School_form(request.POST,'school_form',instance=school)
        if form.is_valid():
            form.save()
            return redirect('school_info')
def school_delete(request,id =0):
    if id != 0:
        school = School.objects.get(pk=id)
        school.delete()
        return redirect('school_info')


# School Lab
def school_lab(requiest):
    context = {'school_lab':School_lab.objects.all()}
    return render(requiest,'school_lab.html',context)

def school_lab_form(request,id=0):
    if request.method == "GET":
        if id ==0:
            form = School_lab_form()
        else:
            school_lab = School_lab.objects.get(id = id )
            form = School_lab_form(instance=school_lab)
        return render(request,'school_lab_form.html', {'form':form})
    else:
        if id ==0:
            form = School_lab_form(request.POST)
        else:
            school_lab = School_lab.objects.get(id=id)
            form = School_lab_form(request.POST, instance=school_lab)
        if form.is_valid():
             form.save()
        return redirect('/school_lab')

def school_lab_delete(request,id=0):
    if id!=0:
        school_lab = School_lab.objects.get(pk=id)
        school_lab.delete()
    return redirect('/school_lab')



def school_lab_computers(request,id=0):
    if id == 0 :
        return render(request, 'school_lab.html')
    else:
        lab = School_lab.objects.get(id = id)
        computer = School_computer.objects.filter(lab = lab)
    return render(request,'school_lab_computers.html',{'computer':computer,'lab':lab})


def school_computer_form(request,lab=0,id=0):
    lab = School_lab.objects.get(id = lab)
    if request.method == "GET":
        if id==0:
            form = School_Computer_Form()
        else:
            computer = School_computer.objects.get(id=id)
            form = School_Computer_Form(instance=computer)

        return render(request, 'school_computer_form.html', {'form': form,'lab':lab})
    else:
        if id == 0 :
            form = School_Computer_Form(request.POST)
        else:
            computer = School_computer.objects.get(pk=id)
            form = School_Computer_Form(request.POST,instance=computer)
        x = form['lab'].value()
        form.save()
        return school_lab_computers(request,x)

def school_computer_delete(request,id=0):
    if id !=0:
        computer = School_computer.objects.get(pk=id)
        my_lab = computer.lab
        x = my_lab.id
        computer.delete()
    return school_lab_computers(request,x)