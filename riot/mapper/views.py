from django.shortcuts import render
from .models import Riot
from .forms import RiotForm


# Create your views here.
def index(request):
    locations = Riot.objects.all()

    current_user = request.user
    if request.method == 'POST':
        form = RiotForm(request.POST,request.FILES)
        if form.is_valid():
            locations = form.save(commit=False)
            locations.user = current_user
            locations.save()

    else:
        form = RiotForm()

    return render(request,'index.html',{"form":form,"locations":locations})
