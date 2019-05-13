from django.contrib import admin
from .models import Blog, Category

class AdminBlog(admin.ModelAdmin):
    list_display = ('title', 'enabled')
    search_fields = ('title', 'enabled')

class  AdminCategory(admin.ModelAdmin):
    list_display = ('title','slug')

admin.site.register(Blog, AdminBlog)
admin.site.register(Category, AdminCategory)