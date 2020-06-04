from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from blog.models import Category, Blog
from home.models import userProfile


def index(request):
    lastBlogs = Blog.objects.all()[:3]
    category = Category.objects.all()
    sliderdata = Blog.objects.all()[:3]
    profile = request.user.id
    context = {'category': category,
               'sliderdata': sliderdata,
               'lastBolgs': lastBlogs,
               'profile': profile}
    return render(request, 'user_profile.html', context)


def changepassword(request):
    category = Category.objects.all()
    userinfo = userProfile.objects.get(user=request.user)
    if request.method == 'POST':
        oldPassword = request.POST.get('oldpassword')
        newPassword = request.POST.get('newpassword')
        if oldPassword != '' and newPassword != '':

            user = authenticate(username=request.user, password=oldPassword)
            if user is not None:
                user = User.objects.get(username=request.user)
                user.set_password(newPassword)
                user.save()
                return redirect('/login')
            else:
                print("nnnnoooooooooooooo")

    context = {
        'category': category
    }
    return render(request, 'change_password.html', context)


def updateprofile(request):
    category = Category.objects.all()
    user = userProfile.objects.get(user=request.user)
    print(user)
    if request.method == 'POST':
        username = request.POST.get('username')
        userphone = request.POST.get('phone')
        useradress = request.POST.get('adress')
        userconutry = request.POST.get('country')
        usercity = request.POST.get('city')
        userimage = request.FILES.get('image')
        b = userProfile.objects.get(user=request.user)
        b.image = userimage
        b.city = usercity
        b.country = userconutry
        b.phone = userphone
        b.save()
        return redirect('/userpage')
    context = {
        'category': category,
        'user': user,
    }
    return render(request, 'update_profile.html', context)
