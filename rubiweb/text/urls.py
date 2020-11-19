from django.urls import path
from django.contrib import admin
from . import views
from . import admin_general


urlpatterns = [
    #path('', views.index, name='index'),

   #admin rubicxontext
   path('admin_general/', admin_general.admin_general, name='admin_general'),
   path('admin_scrap_auto/', admin_general.admin_scrap_auto, name='admin_scrap_auto'),
 
]