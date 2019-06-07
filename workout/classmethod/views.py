from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import productname
from .forms import MyForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

@method_decorator(login_required,name='dispatch')
class allproducts(View):
    template_name='methodfolder/methodlist.html'


    def get(self,request,*args,**kwargs):
        context = {}
        queryset = productname.objects.all()
        context['object']=queryset
        return render(request,self.template_name,context)


class detailproduct(View):
    template_name='methodfolder/methoddetail.html'
    def get(self,request,*args,**kwargs):
        context={}
        id_=self.kwargs.get('id')
        if id_ is not None:
            obj=get_object_or_404(productname,id=id_)
            context['object']=obj
        return render(request,self.template_name,context)


class createproduct(View):
    template_name='methodfolder/methodcreate.html'
    def get(self,request,*args,**kwargs):

        form=MyForm()
        context = {'form':form}
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form=MyForm(request.POST)
        if form.is_valid():
            form.save()
            form = MyForm()
        context={'form':form}

        return render(request,self.template_name,context)


class updateproduct(View):
    template_name='methodfolder/methodupdate.html'

    def get(self,request,*args,**kwargs):
        context={}
        _id=self.kwargs.get('id')
        if _id is not None:
            obj=get_object_or_404(productname,id=_id)
        if obj is not None:
            form=MyForm(instance=obj)
            context['object']=obj
            context['form']=form
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        context={}
        _id = self.kwargs.get('id')
        if _id is not None:
            obj = get_object_or_404(productname, id=_id)
        form=MyForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        context['object']=obj
        context['form']=form

        return render(request,self.template_name,context)

class deleteproduct(View):
    template_name='methodfolder/methoddelete.html'

    def get(self,request,*args,**kwargs):
        id_=self.kwargs.get('id')
        context = {}
        if id_ is not None:
            obj=get_object_or_404(productname,id=id_)
            context['object']=obj
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        id_ = self.kwargs.get('id')
        context = {}
        if id_ is not None:
            obj = get_object_or_404(productname, id=id_)
        if obj is not None:
            obj.delete()
            context['object']=None
            return redirect('/alltitles')

        return render(request,self.template_name,context)




