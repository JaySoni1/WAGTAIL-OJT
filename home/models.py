from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks

from customblocks.blocks import FAQBlock, TestimonialSliderBlock, CallToActionBlock


class HomePage(Page):
    body = StreamField(
        [
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('faq', FAQBlock()),
            ('testimonials', TestimonialSliderBlock()),
            ('cta', CallToActionBlock()),
        ],
        use_json_field=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

