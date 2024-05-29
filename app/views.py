from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *


# Create your views here.




def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Data is Submitted...')
        else:
            return HttpResponse('Invalid data')
    return render (request,'insert_topic.html',d)


def insert_Webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('Data is submitted')
        else:
            return HttpResponse('Invalid data')
    return render (request,'insert_Webpage.html',d)


def insert_AccessRecord(request):
    EAFO=AccessRecord()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecord(request.POST)
        if AFDO.is_valid():
            
            AFDO.save()
            return HttpResponse('Data is submitted')
        else:
            return HttpResponse('Invalid data')
    return render (request,'insert_AccessRecord.html',d)




