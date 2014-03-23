from django import template
from blog.models import Blurb

register = template.Library()

@register.simple_tag
def get_blurb(blurb_name):

	try:
		return Blurb.objects.all().filter(name=blurb_name)[0].content
	except:
		return ''