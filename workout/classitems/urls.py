from django.urls import path,include
from classitems import views
from classitems.views import ItemsListview,ItemsDetailview,ItemsCreateview,ItemsUpdateview,ItemsDeleteview

app_name='classitems'
urlpatterns=[
    path('listview/',ItemsListview.as_view(),name='itemslistview'),
    path('detailsview/<int:id>',ItemsDetailview.as_view(),name='itemsdetailview'),
    path('createview/',ItemsCreateview.as_view(),name='itemscreateview'),
    path('update/<int:id>',ItemsUpdateview.as_view(),name='itemupdateview'),
    path('deleteitem/<int:id>',ItemsDeleteview.as_view(),name='itemdeleteview'),


]