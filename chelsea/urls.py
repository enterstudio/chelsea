from django.conf.urls import patterns, include, url
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page
# feeds
from blog.feeds import LatestEntriesFeed
from blog.models import Blog

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

blogsiteDict = {
    'queryset': Blog.objects.filter(status='published'),
    'date_field': 'display_date',
}
sitemaps = {
    'blog': GenericSitemap(blogsiteDict, priority=0.6),
}

handler404 = 'blog.views.show404'

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.index', name='index'),
    
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[-\w]+)/$', 
    	'blog.views.view_post', 
    	name='view_blog_post'),
	
    url(r'^category/(?P<categorySlug>[^\.]+)', 
		'blog.views.view_category', 
		name='view_blog_category'
	),
	url(r'^feeds/latest/$', LatestEntriesFeed()),
    # url(r'^$', 'chelsea.views.home', name='home'),
    # url(r'^chelsea/', include('chelsea.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^sitemap\.xml$', cache_page(86400)(sitemap), {'sitemaps': sitemaps}),
    url(r'^robots\.txt$', include('robots.urls')),

)
