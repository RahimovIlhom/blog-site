from django.contrib import admin

from .models import Category, Tag, Blog, Comment, Like, Contact


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'category', 'created_time']
    list_filter = ['author', 'category', 'tags']
    search_fields = ['title', 'body', 'author', 'blog']
    prepopulated_fields = {
        'slug': ('title', )
    }


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'body', 'created_time']
    list_filter = ['author', 'blog']
    search_fields = ['body', 'author', 'blog']


class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'blog']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Contact)
