from django.shortcuts import render

from home.models import Setting


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'home'}
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'aboutus.html', context)


def contactus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'contactus.html', context)


def references(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'referances.html', context)
