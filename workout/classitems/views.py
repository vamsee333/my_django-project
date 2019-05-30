from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import newitems
from django.http import Http404
from .forms import Classitemform
from django.urls import reverse
from django.views.generic import(ListView,DetailView,CreateView,UpdateView,DeleteView)
# Create your views here.
class ItemsListview(ListView):
    template_name ='classfiles/newitems_list.html'
    queryset = newitems.objects.all()


class ItemsDetailview(DetailView):
    template_name = 'classfiles/newitems_detail.html'
    #queryset=newitems.objects.all()

    def get_object(self, queryset=None):
        id_=self.kwargs.get('id')
        return get_object_or_404(newitems,id=id_)

class ItemsCreateview(CreateView):
    template_name = 'classfiles/newitems_create.html'
    form_class = Classitemform
    queryset = newitems.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ItemsUpdateview(UpdateView):
    template_name = 'classfiles/newitems_create.html'
    form_class = Classitemform
    queryset = newitems.objects.all()

    def get_object(self, queryset=None):
        id_=self.kwargs.get('id')
        return get_object_or_404(newitems,id=id_)


class ItemsDeleteview(DeleteView):
    template_name = 'classfiles/newitems_delete.html'

    def get_object(self, queryset=None):
        id_=self.kwargs.get('id')
        return get_object_or_404(newitems,id=id_)

    def get_success_url(self):
        return reverse('classitems:itemslistview')