from django.urls import path

from . import views

urlpatterns = [
    # ex: /blog/
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('addcomment/<int:id>/<slug:slug>/', views.addcomment, name='addcomment'),

]
