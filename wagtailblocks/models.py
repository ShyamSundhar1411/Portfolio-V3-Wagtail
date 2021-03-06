from random import choices
from django.db import models
from portfolio.choices import *
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock

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
        template = "wagtailblocks/card_block.html"
class CustomCodeBlock(blocks.StructBlock):
    Source_Code = CodeBlock(label='Source Code', default_language='django')
    class Meta:
        icon = "code"
        label = "Code Block"
class TimelineBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100)
    icon = ImageChooserBlock(required = False)
    text = blocks.TextBlock()
    date = blocks.DateBlock()

    class Meta:
        icon = "placeholder"
        template = "wagtailblocks/timeline_block.html"
class SkillBarBlock(blocks.StructBlock):
    Skill = blocks.CharBlock(max_length=100)
    Percentage = blocks.IntegerBlock(max_value=100)
    ColorScheme = blocks.IntegerBlock(max_value = 5,blank = True,default = 1,choices = ColorSchemeChoices)
    class Meta:
        icon = "form"
        template = "wagtailblocks/skill_bar.html"
    