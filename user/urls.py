from django.urls import path

from . import views

urlpatterns = [
    # ex: /blog/
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('updateprofile',views.updateprofile,name='updateprofile'),
    # path('addcomment/<int:id>/<slug:slug>/', views.addcomment, name='addcomment'),


]
