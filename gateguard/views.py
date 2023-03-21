from django.shortcuts import render,HttpResponse,redirect
from .models import RegisteredPcs
from .form import *
from django.contrib import messages

def home(request):
    return render(request,'gateguard/guardhome.html')

def contact(request):
    if request.method=="POST":
        ins=ContactForm(request.POST)
        id=request.POST['ID_no']
        if RegisteredPcs.objects.filter(ID_no=id).exists():
            messages.error(request,"A User With This ID is Already Registred")
            pass
        else:
            if ins.is_valid():
                ins.save()
                messages.success(request,"A user  Registred Succesfully")
                # print("registered")
                return redirect('contact')
    forms={
    "form": ContactForm()
    }
    return render(request,'gateguard/contact.html',forms)

def searchbar(request):
    if request.method=="POST":
       searched=request.POST['query']
       context={}
       if RegisteredPcs.objects.filter(ID_no=searched).exists():
            result=RegisteredPcs.objects.get(ID_no=searched)
            print(result)
            context={"form": ContactForm() ,'result':result}  
            return render(request,'gateguard/search.html',context)
       else:
            messages.error(request,'User With This ID not Exist')   
            return render(request,'gateguard/search.html')    
    return render(request,'gateguard/search.html')

def update(request,pk):
       
        result=RegisteredPcs.objects.get(id=pk)
        # u_form=PcUpdateForm(request.POST or None, instance=result)
        context = { 'res': result} 
        return render(request, 'gateguard/update.html',context)

def update1(request):
    if request.method=='POST':
        serial=request.POST['serial']
        model_name=request.POST['model_name']
        aa=RegisteredPcs.objects.get(serial=serial)
        aa.serial=serial
        aa.model_name=model_name
        aa.save()
        messages.success(request,'update successfully')
    return render(request, 'gateguard/search.html')


def delete(request,id):
    result = RegisteredPcs.objects.get(id = id)
    result.delete()
    return redirect('searched')

from django.shortcuts import render,HttpResponse,redirect

from .form import *
from django.contrib import messages

def home(request):
    return render(request,'gateguard/guardhome.html')

def contact(request):
    if request.method=="POST":
        ins=ContactForm(request.POST)
        id=request.POST['ID_no']
        if RegisteredPcs.objects.filter(ID_no=id).exists():
            messages.error(request,"A User With This ID is Already Registred")
            pass
        else:
            if ins.is_valid():
                ins.save()
                messages.success(request,"A user  Registred Succesfully")
                # print("registered")
                return redirect('contact')
    forms={
    "form": ContactForm()
    }
    return render(request,'gateguard/contact.html',forms)

def searchbar(request):
    if request.method=="POST":
       searched=request.POST['query']
       context={}
       if RegisteredPcs.objects.filter(ID_no=searched).exists():
            result=RegisteredPcs.objects.get(ID_no=searched)
            print(result)
            context={"form": ContactForm() ,'result':result}  
            return render(request,'gateguard/search.html',context)
       else:
            messages.error(request,'User With This ID not Exist')   
            return render(request,'gateguard/search.html')    
    return render(request,'gateguard/search.html')

def update(request,pk):
       
        result=RegisteredPcs.objects.get(id=pk)
        # u_form=PcUpdateForm(request.POST or None, instance=result)
        context = { 'res': result} 
        return render(request, 'gateguard/update.html',context)

def update1(request):
    if request.method=='POST':
        serial=request.POST['serial']
        model_name=request.POST['model_name']
        aa=RegisteredPcs.objects.get(serial=serial)
        aa.serial=serial
        aa.model_name=model_name
        aa.save()
        messages.success(request,'update successfully')
    return render(request, 'gateguard/search.html')


def delete(request,id):
    result = RegisteredPcs.objects.get(id = id)
    result.delete()
    return redirect('searched')