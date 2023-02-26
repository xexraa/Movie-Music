from django import template
from django.utils.html import format_html


register = template.Library()

@register.simple_tag
def star(class_, rating):
    svg = '''
    <svg xmlns="http://www.w3.org/2000/svg" class="{class_}" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
    </svg>
    '''
    filled_class = 'star--filled'
    stars = []
    for i in range(5):
        if rating > i:
            stars.append(format_html(svg, class_=f'{class_} {filled_class}'))
        else:
            stars.append(format_html(svg, class_=class_))
    return format_html(''.join(stars))


