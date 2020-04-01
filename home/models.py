from django.db import models


# Create your models here.
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
    about_us = models.TextField(blank=True,)
    contact = models.TextField(blank=True,)
    references = models.TextField(blank=True, max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.title
