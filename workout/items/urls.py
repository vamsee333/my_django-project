
from django.urls import path,include
from items import views


app_name='items'
urlpatterns=[

    path('home/', views.Main_home_page, name='first_view'),
    path('add/', views.Add_item, name='Add_item'),
    path('form/', views.Using_from, name='Form'),
    path('search/', views.raw_form, name='search'),
    path('single/<int:id>/', views.single_value, name='single'),
    path('delete/<int:id>/',views.delete_items,name='delete')
]