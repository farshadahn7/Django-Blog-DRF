from django.contrib import admin

from .models import Category, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'author', 'created_date', 'published_date', 'updated_date']
    list_filter = ['author', 'title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_name', 'status']
    list_filter = ['cat_name']