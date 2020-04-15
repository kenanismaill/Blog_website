from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


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
    slug = models.SlugField()
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


class Blog(models.Model):
    STATUS = (
        ('true', 'True'),
        ('false', 'False ')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
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
