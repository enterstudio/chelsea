from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
@stringfilter
def pagebreaker(value, name='pagebreak', is_safe=True):
	searchStr = '<div style="page-break-after: always;"><span style="display: none;">&nbsp;</span></div>'
	
	foundPosition = value.index(searchStr) if searchStr in value else False
	
	if foundPosition:
		return value[:foundPosition]
	else:
		return value