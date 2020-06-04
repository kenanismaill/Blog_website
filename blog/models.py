from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from home.models import userProfile


class Category(MPTTModel):
    STATUS = (
        ('true', 'True'),
        ('false', 'False')
    )
    # author = models.TextField(max_length=50)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    content = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '--> '.join(full_path[::-1])

    def image_tag(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img src="{}" height="50" width="100"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class BlogLike(models.Model):
    blog = models.ForeignKey('Blog', null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(userProfile, null=True, blank=True, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog.title


class Blog(models.Model):
    STATUS = (
        ('true', 'True'),
        ('false', 'False ')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(unique=True, null=False)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    detail = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img src="{}" height="50" width="100"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    @property
    def get_likes(self):
        return BlogLike.objects.filter(blog=self)

    @property
    def images(self):
        return Images.objects.filter(Blog=self)


class Images(models.Model):
    Blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img src="{}" height="50" width="100"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class Comment(models.Model):
    STATUS = (
        (' New', 'New'),
        ('true', 'True'),
        ('false', 'False ')
    )

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=50, blank=True)
    comment = models.TextField(max_length=200, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'email', 'website', 'comment']
