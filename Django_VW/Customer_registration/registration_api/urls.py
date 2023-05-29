from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('CustInfo/', home),
    path('RegisterUser', post_Customer),
    path('Update/<int:id>', update_Customer),
    path('Delete/<int:id>', delete_customer),
    path('search/', search_list),
    

]
