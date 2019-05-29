from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import item
from items.forms import Itemsform
from django.http import Http404
#import pdb
#settrace = pdb.set_trace()
# Create your views here.

def Main_home_page(request):
    value=item.objects.all()
    htmlvalue='<h1>verify your account in gmail</h1>'
    return render(request,'MainHome.html',{'value':value,'htmlvalue':htmlvalue})

def single_value(request,id):

    try:
        value=item.objects.get(pk=id)
    except item.DoesNotExist:
        raise Http404
    #value=get_object_or_404(item,id)

    return render(request,'singleitem.html',{'x':value})


def Add_item(request):
    context={
        'title':'books',
        'description':'friction',
        'price':250.50
    }
    item.objects.create(**context)
    return render(request,'AddItem.html',{'context':context})

def Using_from(request):
    initial_data='initial details'
    form=Itemsform()
    form=Itemsform(request.POST or None)
    if form.is_valid():
        form.save()
    context={"form":form}
    return render(request,'form_display.html',context)
def raw_form(request):
    context={}
    return render(request,'searchform.html',context)


def delete_items(request,id):
    obj=get_object_or_404(item,id=id)
    if request.method=='GET':
        x="get method"
    if request.method=='POST':
        obj.delete()
        return redirect('../../home/')
    return render(request,'delete_item.html',{'obj':obj,'x':x})