from django import template
from wagtail.rich_text import expand_db_html

register = template.Library()

@register.simple_tag(takes_context=True)
def render_streamfield(context, stream_value):
    """Render a StreamField with support for our custom blocks.

    This helper keeps the demo template nice and small.
    """
    if not stream_value:
        return ""
    # Use the built-in render for each block
    rendered = []
    for block in stream_value:
        html = block.block.render(block.value, context=context)
        rendered.append(html)
    return "".join(rendered)

@register.filter
def richtext(value):
    """Shortcut for expanding Wagtail rich text in custom templates."""
    return expand_db_html(value)

