import json

from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from blog.models import Blog, Category, Images, Comment
from home.form import SearchForm
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
               'sliderdata': sliderdata, }
    return render(request, 'aboutus.html', context)


def contactus(request):
    form = contactusform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.warning(request, 'Form submission successful')
        return HttpResponseRedirect('/contactus')
    setting = Setting.objects.get(pk=1)
    sliderdata = Blog.objects.all()[:3]
    form = contactusform()
    category = Category.objects.all()
    context = {'setting': setting, 'form': form,
               'category': category,
               'sliderdata': sliderdata, }
    return render(request, 'contactus.html', context)


def references(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Blog.objects.all()[:3]
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'sliderdata': sliderdata, }
    return render(request, 'referances.html', context)


def category_blogs(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    sliderdata = Blog.objects.all()[:3]
    blogs = Blog.objects.filter(category_id=id)
    context = {'blogs': blogs,
               'category': category,
               'sliderdata': sliderdata,
               'categorydata': categorydata}
    return render(request, 'blogs.html', context)


def blog_detail(request, id, slug):
    category = Category.objects.all()
    blog = Blog.objects.get(pk=id)
    images = Images.objects.filter(Blog_id=id)
    comments = Comment.objects.filter(blog_id=id, status='true')
    context = {'blog': blog,
               'category': category,
               'images': images,
               'comments': comments,
               }
    return render(request, 'blog_detail.html', context)


def blog_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        # print(form.errors)
        if form.is_valid():
            category = Category.objects.all()
            sliderdata = Blog.objects.all()[:3]
            query = form.cleaned_data['query']
            blogs = Blog.objects.filter(title__icontains=query)
            context = {'blogs': blogs,
                       'category': category,
                       'sliderdata': sliderdata,
                       }

            return render(request, 'blogs_search.html', context)

    return HttpResponseRedirect('/')


def blog_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        blog = Blog.objects.filter(title__icontains=q)
        results = []
        for rs in blog:
            blog_json = {}
            blog_json = rs.title
            results.append(blog_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_views(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "check your username or password")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {'category': category,
               }
    return render(request, 'login.html', context)
