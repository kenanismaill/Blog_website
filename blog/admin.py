from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from blog.models import Category, Blog, Images, Comment, BlogLike


class BlogImageInline(admin.TabularInline):
    model = Images
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['status']


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_blogs_count', 'related_blogs_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Blog,
            'category',
            'blogs_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                Blog,
                                                'category',
                                                'blogs_count',
                                                cumulative=False)
        return qs

    def related_blogs_count(self, instance):
        return instance.blogs_count

    related_blogs_count.short_description = 'Related blogs (for this specific category)'

    def related_blogs_cumulative_count(self, instance):
        return instance.blogs_cumulative_count

    related_blogs_cumulative_count.short_description = 'Related blogs (in tree)'


admin.site.register(Category, CategoryAdmin2)

class BlogLikeAdmin(admin.ModelAdmin):
    list_display = ['blog', 'user', 'created_on']
    list_filter = ['created_on']

admin.site.register(BlogLike, BlogLikeAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category']
    inlines = [BlogImageInline]
    prepopulated_fields = {'slug': ('title',)}

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'Blog', 'image_tag']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'email', 'status', 'comment']
    list_filter = ['status']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Comment, CommentAdmin)
