from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
# Create your models here.
class ResponsiveImageBlock(ImageChooserBlock):
    class Meta:
        icon = "image"
        template = "wagtailblocks/responsive_image_block.html"
class CardBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock()
    body = blocks.TextBlock()
    page_link = blocks.PageChooserBlock()

    class Meta:
        icon = "placeholder"
        template = "streamfieldblocks/card_block.html"