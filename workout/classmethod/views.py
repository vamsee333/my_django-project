from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import productname
from .forms import MyForm
# Create your views here.

class allproducts(View):
    template_name='methodfolder/methodlist.html'
    queryset=productname.objects.all()

    def get(self,request,*args,**kwargs):
        context = {}
        context['object']=self.queryset
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
