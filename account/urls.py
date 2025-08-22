from django.urls import path
from account import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('second_page',views.second_page,name='second_page'),
    path('third_page',views.third_page,name='third_page'),
    path('imagepage',views.imagepage,name='imagepage'),
    path('imagepage2',views.imagepage2,name='imagepage2'),
    path('imagepage3/<str:imagesname>',views.imagepage3,name='imagepage3')
]
