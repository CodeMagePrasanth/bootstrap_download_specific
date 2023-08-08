from django.shortcuts import render

# Create your views here.

def bootstarp_download(request):
    return render(request,'bootstarp_download.html')

def Cards(request):
    return render(request,'Cards.html')