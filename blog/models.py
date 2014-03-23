from django.db import models
from django.db.models import permalink
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from model_utils import Choices

from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class Blog(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = RichTextField(config_name='awesome_ckeditor')
    address = models.CharField(max_length=200,null=True, blank=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    display_date = models.DateTimeField(db_index=True)
    
    STATUSES = Choices('draft', 'published')
    status = models.CharField(choices=STATUSES, default=STATUSES.draft, max_length=20)
    # category = models.ForeignKey('blog.Category', blank=True, null=True, on_delete=models.SET_NULL)
    
    categories = models.ManyToManyField(Category, blank=True, null=True, through='CategoryToPost')

    main_photo_description = 'Main Image - will be displayed for blog post. Keep to 800px wide'
    main_photo = models.ImageField(main_photo_description,upload_to='pics', null=True, blank=True)
    
    main_photo_alt_text_short_description = 'Image alt text - type image alternate text - image description here.'
    main_photo_alt_text = models.CharField(main_photo_alt_text_short_description, max_length=200, null=True, blank=True)
    
    # main_photo_credit = models.CharField(max_length=100, null=True, blank=True)
    
    author = models.ForeignKey(User)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 
                                        'year':self.display_date.year,
                                        'month':self.display_date.strftime("%m"),
                                        'slug': self.slug 
                                        })

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
            

        super(Blog, self).save(*args, **kwargs)

    def admin_main_photo(self):
        if self.main_photo:
            return '<img width="180" src="https://chchchelsea.s3.amazonaws.com/%s"/>' % self.main_photo
        else:
            return ''
    admin_main_photo.allow_tags = True

    def s3_main_image_url(self):
        if self.main_photo:
            return 'http://chchchelsea.s3.amazonaws.com/%s' % self.main_photo
        else:
            return ''

class CategoryToPost(models.Model):
    post = models.ForeignKey(Blog)
    category = models.ForeignKey(Category)

class Blurb(models.Model):
  name = models.CharField(max_length=25,unique=True, db_index=True)
  content = RichTextField(config_name='awesome_ckeditor')

class Photo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    posted = models.DateField(db_index=True, auto_now_add=True)
    file = models.ImageField(upload_to='pics')
    
    def __unicode__(self):
        return '%s' % self.title