from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,UpdateView,CreateView,DeleteView,DetailView
# Create your views here.
def home(request):
    # return HttpResponse('Bonjour <i>5TWIN 2</i>')
    return render(request,template_name='Event/home.html')
@login_required(login_url="log")
def listEvent(request):
    events=Event.objects.all().order_by('-evt_date')
    return render(request,"Event/list.html",{'evt':events})
class Affiche(ListView):
    model=Event
    # template_name="Event/list.html"
    context_object_name="evt"
    ordering=['-title']