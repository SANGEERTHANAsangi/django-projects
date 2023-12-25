from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def allocategories(request):
    # return render(request,'category.html')
    c=Category.objects.all()
    return render(request,'category.html',{'shops':c})
def allproducts(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request,'product.html',{'c':c,'p':p})

def detail(request,p):
    product=Product.objects.get(name=p)
    return render(request,'detail.html',{'p':product})
def registration(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        if (p == cp):
            us=User.objects.create_user(username=u,password=p,email=e)
            us.save()
            return redirect('shop:allocate')
        else:
            messages.error(request, "Passwords are not matching")
    return render(request,'register.html')


def user_login(request):
    if(request.method=="POST"):
        name=request.POST['un']
        pass1=request.POST['pas']
        user=authenticate(username=name,password=pass1)
        if user:
            login(request,user)
            return redirect('shop:allocate')
        else:
            messages.error(request,"Invalid Credintails")
    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    return user_login(request)
