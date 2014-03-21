from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blog.models import Blog

class LatestEntriesFeed(Feed):
    title = "Chelsea Feed Test"
    link = "/"
    description = "Test description ..."

    def items(self):
        return Blog.objects.order_by('-display_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('view_blog_post', args=[item.display_date.year, item.display_date.strftime("%m"),item.slug])