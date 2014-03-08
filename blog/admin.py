from django.contrib import admin
from blog.models import Blog, Category,Photo


class BlogPhotoInline(admin.TabularInline):
    model = Photo
    extra = 3

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ BlogPhotoInline, ]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog)
admin.site.register(Category)
