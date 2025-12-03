from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class FAQItemBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True, help_text="FAQ question")
    answer = blocks.RichTextBlock(required=True, help_text="FAQ answer")

    class Meta:
        icon = "help"
        label = "FAQ Item"

class FAQBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, default="Frequently Asked Questions")
    items = blocks.ListBlock(FAQItemBlock(), help_text="Add FAQ question/answer pairs")

    class Meta:
        icon = "help"
        label = "FAQ Section"
        template = "customblocks/blocks/faq_block.html"

class TestimonialBlock(blocks.StructBlock):
    quote = blocks.TextBlock(required=True, help_text="Testimonial text")
    name = blocks.CharBlock(required=True, help_text="Person's name")
    role = blocks.CharBlock(required=False, help_text="Role / Company")
    avatar = ImageChooserBlock(required=False)

    class Meta:
        icon = "user"
        label = "Testimonial"

class TestimonialSliderBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, default="What our customers say")
    testimonials = blocks.ListBlock(TestimonialBlock(), min_num=1)

    class Meta:
        icon = "group"
        label = "Testimonial Slider"
        template = "customblocks/blocks/testimonial_slider.html"

class CallToActionBlock(blocks.StructBlock):
    eyebrow = blocks.CharBlock(required=False, help_text="Small text above headline")
    headline = blocks.CharBlock(required=True)
    body = blocks.RichTextBlock(required=False)
    button_text = blocks.CharBlock(required=True, default="Get started")
    button_url = blocks.URLBlock(required=True)
    secondary_link_text = blocks.CharBlock(required=False)
    secondary_link_url = blocks.URLBlock(required=False)

    class Meta:
        icon = "placeholder"
        label = "Call to Action"
        template = "customblocks/blocks/call_to_action.html"

