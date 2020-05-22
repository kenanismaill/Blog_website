from django.contrib.auth.models import User
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe


class Setting(models.Model):
    STATUS = (
        ('true', 'True'),
        ('false', 'False')
    )
    # author = models.TextField(max_length=50)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    adress = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=50)
    fax = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=50)
    smptemail = models.CharField(blank=True, max_length=50)
    smptpassword = models.CharField(blank=True, max_length=50)
    smptport = models.CharField(blank=True, max_length=50)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    about_us = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed')
    )
    name = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=150)
    note = models.CharField(blank=True, max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class contactusform(forms.ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'text', 'placeholder': 'Name & SurName'}),
            'email': forms.TextInput(attrs={'class': 'text', 'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'class': 'text', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'text', 'placeholder': 'Name & SurName', 'rows': '10'})
        }


class userProfile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    phone= models.CharField(blank=True,max_length=50)
    adress = models.CharField(blank=True, max_length=150)
    country = models.CharField(blank=True, max_length=50)
    city = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True,upload_to='images/users/')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return '['+self.user.username + '] '+self.user.first_name

    def image_tag(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img src="{}" height="50" width="100"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

class userProfileForm(ModelForm):
    class Meta:
        model = userProfile
        fields = ['phone','adress','country','city','image',]
