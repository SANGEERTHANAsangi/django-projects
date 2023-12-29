from django.shortcuts import render,redirect
from movies.models import nav
from movies.forms import navform

def home(request):
    m=nav.objects.all()
    return render(request,'base.html',{'m':m})
def base1(request):
    if(request.method=='POST'):
        n=request.POST['n']
        d=request.POST['d']
        im=request.FILES['i']
        m=nav.objects.create(name=n,des=d,image=im)
        m.save()
        return home(request)
    return render(request, 'home.html')
def gosomewhere(request,p):
    n=nav.objects.get(name=p)
    return render(request,'gosomewhere.html',{'n':n})
def delete(request,p):
    o=nav.objects.get(name=p)
    o.delete()
    return redirect('movies:home')

def edit(request,p):
    b = nav.objects.get(name=p)
    form = navform(instance=b)
    if (request.method == "POST"):
        form = navform(request.POST, request.FILES, instance=b)
        if (form.is_valid()):
            form.save()
            return home(request)
    return render(request, 'edit.html', {'form': form})
