from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Datas
# Create your views here.

def home(request):
    mydata=Datas.objects.all()
    if(mydata!=''):
       return render(request,'home.html',{'datas':mydata})
    else:
       return render(request,'home.html')


def addData(request):
    if request.method=='POST':
        name=request.POST['name']
        contactnumber=request.POST['contactnumber']

        obj=Datas()
        obj.name=name
        obj.contactnumber=contactnumber
        obj.save()
        mydata=Datas.objects.all()
        messages.success(request,'Registration Successfully completed')
        return redirect('home')
    return render(request,'home.html')

def updateData(request,id):
    mydata=Datas.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        contactnumber=request.POST['contactnumber']

        mydata.name=name
        mydata.contactnumber=contactnumber
        mydata.save()
        messages.success(request,'Upate Successfully Completed')
        return redirect('home')
    return render(request,'update.html',{'data':mydata})

def deleteData(request,id):
    mydata=Datas.objects.get(id=id)
    mydata.delete()
    messages.error(request,'Deleted Successfully Completed')
    return redirect('home')