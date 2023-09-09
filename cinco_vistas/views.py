from django.shortcuts import render

# Create your views here.


def campeones(request):
    return render(request,'campeones.html')

def home(request):
    return render(request,'home.html')

def items(request):
    return render(request,'items.html')

