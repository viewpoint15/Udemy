from django.urls import path
from account import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('second_page',views.second_page,name='second_page')
]
