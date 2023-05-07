from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .forms import ComputerForm,CopierForm,PrinterForm,ProjectorForm,FiberForm,IPForm,WifiForm,School_lab_form,School_form,School_Computer_Form
from .models import Doe_computer,Doe_copier,Doe_printer,Doe_projector,Doe_Fiber,Doe_Wifi,Common_Ip,School_lab,School,School_computer
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

def doe(request):
    return render(request,'doe.html')

def doe_computer(request):
    context = {'doe_computer': Doe_computer.objects.all()}
    return render(request,'doe_computer.html',context)



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