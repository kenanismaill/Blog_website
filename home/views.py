from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from blog.models import Blog, Category
from home.models import Setting, contactusform


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Blog.objects.all()[:3]
    category = Category.objects.all()

    context = {'setting': setting, 'page': 'home',
               'sliderdata': sliderdata,
               'category': category}
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Blog.objects.all()[:3]
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'sliderdata': sliderdata,}
    return render(request, 'aboutus.html', context)


def contactus(request):
    form = contactusform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.Info(request, 'Form submission successful')
        return HttpResponseRedirect('/contactus')
    setting = Setting.objects.get(pk=1)
    sliderdata = Blog.objects.all()[:3]
    form = contactusform()
    category = Category.objects.all()
    context = {'setting': setting, 'form': form,
               'category': category,
               'sliderdata': sliderdata,}
    return render(request, 'contactus.html', context)


def references(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Blog.objects.all()[:3]
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'sliderdata': sliderdata,}
    return render(request, 'referances.html', context)


def category_blogs(request,id,slug):
    category = Category.objects.all()[:3]
    categorydata = Category.objects.get(pk=id)
    sliderdata = Blog.objects.all()
    blogs = Blog.objects.filter(category_id=id)
    context = {'blogs': blogs,
               'category': category,
               'sliderdata': sliderdata,
               'categorydata': categorydata}
    return render(request, 'blogs.html', context)
