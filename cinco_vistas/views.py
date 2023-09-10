from django.shortcuts import render
from .models import Video
# Create your views here.


def campeones(request):
    return render(request,'campeones.html')

def home(request):
    return render(request,'home.html')

def items(request):
    return render(request,'items.html')

def plays(request):
    videos = Video.objects.all()
    return render(request,'plays.html', context = {'videos': videos})