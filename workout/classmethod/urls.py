from django.urls import path,include
from .views import allproducts,detailproduct,createproduct,updateproduct,deleteproduct
urlpatterns=[
    path('alltitles/',allproducts.as_view(),name='allproducts'),
    path('detailtitle/<int:id>',detailproduct.as_view(),name='detailproducts'),
    path('createtitle',createproduct.as_view(),name='createproducts'),
    path('updatetitle/<int:id>',updateproduct.as_view(),name='updateproduct'),
    path('deletetitle/<int:id>',deleteproduct.as_view(),name='deleteproduct'),
]