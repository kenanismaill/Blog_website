from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from blog.models import Blog
from home.models import Setting, contactusform


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Blog.objects.all()
    context = {'setting': setting, 'page': 'home',
               'sliderdata': sliderdata}
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'aboutus.html', context)


def contactus(request):
    form = contactusform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.Info(request, 'Form submission successful')
        return HttpResponseRedirect('/contactus')
    setting = Setting.objects.get(pk=1)
    form = contactusform()
    context = {'setting': setting, 'form': form}
    return render(request, 'contactus.html', context)


def references(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'referances.html', context)
