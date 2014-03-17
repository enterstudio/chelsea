# Create your views here.

from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    template_data = {
        'categories': Category.objects.all(),
        'posts': Blog.objects.filter(status='published').order_by('-posted')[:5],
        'baseContainerClasses' : ['blog_page']
    }
    return render_to_response('index.html',template_data)

def view_post(request, slug, year, month,):   
    template_data = {
        'post': get_object_or_404(Blog, slug=slug),
        'baseContainerClasses' : ['blog_page','blog_item']
    }
    return render_to_response('blog_entry.html', template_data)

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })
