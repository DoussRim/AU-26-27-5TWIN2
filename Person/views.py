from django.shortcuts import render,redirect
from .forms import FormRegistration
from django.contrib.auth import login
# Create your views here.
def SignUp(request):
    if request.method=="POST":
        form=FormRegistration(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("h")
    else:
            form=FormRegistration()
    return render(request,'Person/Register.html',{"ff":form})
            
