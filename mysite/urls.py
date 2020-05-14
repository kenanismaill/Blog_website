"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path, include
import os

from home import views

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
urlpatterns = [
    path('', include('home.urls')),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('referance', views.references, name='referance'),
    path('home/', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>/', views.category_blogs, name='category_blogs'),
    path('blog/<int:id>/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('search/', views.blog_search,name= 'blog_search'),
    path('search_auto/',views.blog_search_auto,name='blog_search_auto'),
    path('logout/',views.logout_views,name='logout_views'),
    path('login/',views.login_views,name='login_views'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
