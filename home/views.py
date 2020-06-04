import json

from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from blog.models import Blog, Category, Images, Comment, BlogLike
from home.form import SearchForm, RegisterForm
from home.models import Setting, contactusform, userProfile


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Blog.objects.all()[:3]
    category = Category.objects.all()
    lastBlogs = Blog.objects.all()[:2]
    blog = Blog.objects.all()[:10]
    context = {'setting': setting, 'page': 'home',
               'sliderdata': sliderdata,
               'category': category,
               'lastBlogs': lastBlogs,
               'blog': blog, }
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Blog.objects.all()[:3]
    category = Category.objects.all()
    lastBlogs = Blog.objects.all()[:1]
    context = {'setting': setting,
               'category': category,
               'sliderdata': sliderdata,
               'lastBlogs': lastBlogs}
    return render(request, 'aboutus.html', context)


def contactus(request):
    form = contactusform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "your comment has sent successfly ")
        return HttpResponseRedirect('/contactus')
    setting = Setting.objects.get(pk=1)
    sliderdata = Blog.objects.all()[:3]
    lastBlogs = Blog.objects.all()[:3]
    form = contactusform()
    category = Category.objects.all()
    context = {'setting': setting, 'form': form,
               'category': category,
               'sliderdata': sliderdata,
               'lastBlogs': lastBlogs}
    return render(request, 'contactus.html', context)


def references(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Blog.objects.all()[:3]
    category = Category.objects.all()
    lastBlogs = Blog.objects.all()[:2]
    context = {'setting': setting,
               'category': category,
               'sliderdata': sliderdata,
               'lastBlogs': lastBlogs}
    return render(request, 'referances.html', context)


def category_blogs(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    sliderdata = Blog.objects.all()[:3]
    lastBlogs = Blog.objects.all()[:2]
    blogs = Blog.objects.filter(category_id=id)
    context = {'blogs': blogs,
               'category': category,
               'sliderdata': sliderdata,
               'categorydata': categorydata,
               'lastBlogs': lastBlogs}
    return render(request, 'blogs.html', context)


def blog_detail(request, id, slug):
    category = Category.objects.all()

    blog = Blog.objects.get(pk=id)
    lastBlogs = Blog.objects.all()[:2]
    images = Images.objects.filter(Blog_id=id)
    comments = Comment.objects.filter(blog_id=id, status='true')
    if request.user.is_authenticated:
        profile = userProfile.objects.get(user=request.user)
        didLiked = BlogLike.objects.filter(blog=blog, user=profile)
    else:
        profile = None
        didLiked = False
    context = {'blog': blog,
               'category': category,
               'images': images,
               'comments': comments,
               'lastBlogs': lastBlogs,
               'profile': profile,
               'didLiked': didLiked
               }
    return render(request, 'blog_detail.html', context)


def blog_like_unlike(request, id, slug):

    blog = Blog.objects.get(pk=id)
    profile = userProfile.objects.get(user=request.user)
    blogLike = BlogLike.objects.filter(blog=blog, user=profile)
    if len(blogLike) == 0:
        BlogLike(blog=blog, user=profile).save()
    else:
        blogLike.delete()

    return redirect(f'/blog/{id}/{slug}/')


def blog_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        # print(form.errors)
        if form.is_valid():
            category = Category.objects.all()
            sliderdata = Blog.objects.all()[:3]
            # lastBlogs = Blog.objects.all()[:3]
            query = form.cleaned_data['query']
            blogs = Blog.objects.filter(title__icontains=query)
            context = {'blogs': blogs,
                       'category': category,
                       'sliderdata': sliderdata,
                       }

            return render(request, 'blogs_search.html', context)

    return HttpResponseRedirect('/')


def blog_search_auto(request):
    query = request.GET.get('query')
    if query is None:
        return HttpResponse(json.dumps({}))
    if len(query) == 0:
        return HttpResponse(json.dumps({}))
    blogs = Blog.objects.filter(title__icontains=query)
    result = {}
    for blog in blogs:
        result[blog.id] = [blog.slug, blog.title]
    return HttpResponse(json.dumps(result))


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


def register_views(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']

            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')

    form = RegisterForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form,
               }
    return render(request, 'register.html', context)


def userpage(request):
    category = Category.objects.all()
    profile = userProfile.objects.get(user=request.user)
    context = {'category': category,
               'profile': profile
               }
    # print(profile.username)
    return render(request, 'user_info.html', context)


def useraddblog(request):
    category = Category.objects.all()
    profile = userProfile.objects.get(user_id=request.user.id)

    context = {'category': category,
               'profile': profile
               }
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        keywords = request.POST.get('keywords')
        detail = request.POST.get('detail')
        status = request.POST.get('status')
        categoryId = request.POST.get('category')
        image = request.FILES.get('image')
        category2 = Category.objects.get(pk=categoryId)
        if status == 0:
            status = "hayir"
        else:
            status = "evet"
        auther = request.POST.get('auther')
        user = User.objects.get(username=request.user)

        b = Blog(category=category2, user=user, author=auther, title=title, keywords=keywords, description=description,
                 image=image, status=status, slug=title + "-slug", parent=None, detail=detail)
        b.save()
        return redirect('/home/')
    return render(request, 'user_add_blog.html', context)


def userblogs(request):
    category = Category.objects.all()
    user = request.user
    myblogs = Blog.objects.filter(user_id=user.id)
    print(myblogs)
    context = {'category': category,

               'myblogs': myblogs,
               }
    return render(request, 'userblogs.html', context)


def usercomments(request):
    category = Category.objects.all()
    user = request.user
    mycomments = Comment.objects.filter(user_id=user.id)
    context = {'category': category,

               'mycomments': mycomments,
               }
    return render(request, 'usercomments.html', context)


def question(request):
    return HttpResponse("question page ")
