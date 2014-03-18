from django.contrib import admin
from blog.models import Blog, Category, CategoryToPost
from django.contrib.auth.models import User

from datetime import datetime

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

class CategoryToPostInline(admin.TabularInline):
	model = CategoryToPost
	extra = 1

class BlogAdmin(admin.ModelAdmin):

	list_display = ['title', 'admin_main_photo','posted','display_date','status']
	fields = ('title','slug','display_date','body','address','main_photo','main_photo_alt_text','status')
	prepopulated_fields = {"slug": ("title",)}
	exclude = ('author',)
	inlines = [CategoryToPostInline]


	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()
	


admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)

# class PhotoAdmin(admin.ModelAdmin):
# 	fields = ('title','description','file',)

# admin.site.register(Photo, PhotoAdmin)
