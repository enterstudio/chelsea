from django.db import models
from django.db.models import permalink
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from model_utils import Choices

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = RichTextField(config_name='awesome_ckeditor')
    posted = models.DateField(db_index=True, auto_now_add=True)
    
    STATUSES = Choices('draft', 'published')
    status = models.CharField(choices=STATUSES, default=STATUSES.draft, max_length=20)
    category = models.ForeignKey('blog.Category')
    
    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Blog, self).save(*args, **kwargs)

class Photo(models.Model):
    blogpost = models.ForeignKey(Blog, related_name='images')
    file = models.ImageField(upload_to='pics')
    

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })