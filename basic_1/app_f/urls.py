from django.urls import path
from .views.functionbase_views import book_list , Coverpage


urlpatterns = [
    path('functionbase_views/',book_list ,name ='book_list'),
    path('functionbase_views/',Coverpage ,name ='coverpage'),
    

]                            