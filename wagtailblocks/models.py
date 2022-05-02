from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
# Create your models here.
class ResponsiveImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    image_caption = blocks.RichTextBlock(classname = "caption",required=False)
    class Meta:
        icon = "image"
class CardBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock()
    body = blocks.TextBlock()
    page_link = blocks.PageChooserBlock()

    class Meta:
        icon = "placeholder"
        template = "streamfieldblocks/card_block.html"