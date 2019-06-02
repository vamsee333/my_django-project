from django.urls import path,include
from .views import allproducts,detailproduct,createproduct
urlpatterns=[
    path('alltitles/',allproducts.as_view(),name='allproducts'),
    path('detailtitle/<int:id>',detailproduct.as_view(),name='detailproducts'),
    path('createtitle',createproduct.as_view(),name='createproducts'),
]