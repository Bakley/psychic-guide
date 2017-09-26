# from django.http import HttpResponse
from django.shortcuts import render

from .models import Sender, Receiver, Parcel


def home(request):
    parcel = Parcel.objects.all()
    context = {'parcel': parcel}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def location(request):
    return render(request, 'location.html')


def contact(request):
    return render(request, 'contact.html')
