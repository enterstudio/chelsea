from django.contrib import admin
from blog.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):

	list_display = ['title', 'admin_main_photo','posted','status']
	fields = ('title','slug','body','address','main_photo','main_photo_alt_text','category','status')
	prepopulated_fields = {'slug': ('title',)}
	# exclude = ('posted',)
	


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)

# class PhotoAdmin(admin.ModelAdmin):
# 	fields = ('title','description','file',)

# admin.site.register(Photo, PhotoAdmin)
