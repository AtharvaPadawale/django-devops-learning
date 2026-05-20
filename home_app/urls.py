from django.urls import path
from .views import *

urlpatterns = [
    path ("", index_page),
    path ("index_new/", index_new), 
    
]

