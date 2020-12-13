from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .forms import ComputerForm,CopierForm,PrinterForm
from .models import Doe_computer,Doe_copier,Doe_printer
# Create your views here.

def index(request):
    return render(request,'index.html')

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