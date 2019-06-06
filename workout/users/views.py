from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib import messages
# Create your views here.

# class Register(View):
#     template_name='user/registerUser.html'
#
#     def get(self,request,*args,**kwargs):
#         form=  UserCreationForm()
#         context={}
#         context['form']=form
#         return  render(request,self.template_name,context)
#
#     def post(self,request,*args,**kwargs):
#         form= UserCreationForm(request.POST)
#         context = {}
#
#         if form.is_valid():
#             form.save()
#             context['form']=form
#             redirect('alltitles/')
#         else:
#             redirect('alltitles/')
#         return render(request,self.template_name,context)

from django.contrib.auth.forms import UserCreationForm
from .forms import userdefinedform
def Register(request):


    if request.method =='POST':
        print('hi')
        form = userdefinedform(request.POST)
        if form.is_valid():
            form.save()
    else:
        print('get')
        form = userdefinedform()

    return render(request,'user/registerUser.html',{'form':form})


class reg (View):
    template_name='user/registerUser.html'

    def get(self,request,*args,**kwargs):
        form=userdefinedform()
        context={}
        context['form']=form
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form=userdefinedform(request.POST)
        context={}
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'hello you have created {username}')
            return redirect('../../alltitles/')
        context['form']=form
        return render(request,self.template_name,context)
