from django.shortcuts import render,HttpResponse
from .forms import Register
# Create your views here.
def info(request):
    f=Register()
    if request.method=='POST':
        f1=Register(request.POST)
        if f1.is_valid():
            print(f1.cleaned_data['name'])
            print(f1.cleaned_data['age'])
    return render(request,'register.html',{'forms':f})