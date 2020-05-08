from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from blog.models import CommentForm, Comment


def index(request):
    return HttpResponse("welcome to Blog page")


@login_required(login_url='/login')
def addcomment(request, id,slug):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = Comment()
            data.user_id = current_user.id
            data.blog_id = id
            data.blog_slug=slug
            data.subject = form.cleaned_data['subject']
            data.email = form.cleaned_data['email']
            data.website = form.cleaned_data['website']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.Info(request, "your mesaj has successfly sent")
            return HttpResponseRedirect(url)
    messages.Warning(request, "did not send , please check fields")
    return HttpResponseRedirect(url)
