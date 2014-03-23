from django.core.cache import get_cache
from django.contrib.sitemaps import Sitemap
from blog.models import Blog

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
    	return Blog.objects.filter(status='published').order_by('-display_date')

    def lastmod(self, obj):
        return obj.display_date