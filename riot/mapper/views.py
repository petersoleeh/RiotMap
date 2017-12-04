from django.shortcuts import render
from .models import Riot
from .forms import RiotForm


# Create your views here.
def index(request):
    form = RiotForm()
    return render(request,'index.html',{"form":form})
