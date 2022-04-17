from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    Hero_Title = models.CharField(max_length=200,blank=True)
    Hero_Summary = RichTextField()
    Profile_Pic = models.ForeignKey("wagtailimages.Image",blank = False,null = True,on_delete=models.SET_NULL)
    content_panels = Page.content_panels + [
        FieldPanel("Hero_Title"),
        FieldPanel("Hero_Summary",classname = "full"),
        ImageChooserPanel("Profile_Pic"), 
        
        
    ]