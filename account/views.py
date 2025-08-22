from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.
def index(request):
    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    # else:
    #     form = UserForm()
    return render(request,'index.html')

def second_page(request):
    return render(request,'second_page.html')

def third_page(request):
    var = 'Hello Professor'
    fruits = ["apple","grasps","mango"]
    num1 , num2  = 3,4
    ans = num1 > num2
    memory = {
        'var' : var,
        'fruits': fruits,
        'num1': num1,
        'num2': num2,
        'ans': ans
    }
    return render(request,'third_page.html',context = memory)

def imagepage(request):
    return render(request,'imagepage.html')

def imagepage2(request):
    return render(request,'imagepage2.html')

def imagepage3(request,imagesname):
    imagename = str(imagesname);
    imagename = imagename.lower();
    print(imagename)
    if imagename == "Abstract ironman.jpg":
        var = True
    else:
        imagename == "UltrA  MAX series.jpg" 
        var = False
    memory ={
        'var': var
    }   
    return render(request,'imagepage3.html',context = {'var': var})