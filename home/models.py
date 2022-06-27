from django.db import models
from portfolio.choices import *
from wagtail.core.models import Page
from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel


class HomePageTag(TaggedItemBase):
    content_object = ParentalKey("home.HomePage",on_delete=models.CASCADE, related_name='tagged_items')
class HomePage(Page):
    Hero_Title = models.CharField(max_length=200,blank=True)
    Hero_Summary = RichTextField()
    Profile_Pic = models.ForeignKey("wagtailimages.Image",blank = False,null = True,on_delete=models.SET_NULL)
    Tags = ClusterTaggableManager(through=HomePageTag, blank=True) 
    ColorScheme = models.IntegerField(default = 1,blank = True,choices = ColorSchemeChoices)
    Resume = models.URLField(blank = True,null = True)
    Button_Router = models.ForeignKey(
        'wagtailcore.page',
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="Button Router."
    )
    content_panels = Page.content_panels + [
        FieldPanel("Hero_Title"),
        FieldPanel("Hero_Summary",classname = "full"),
        FieldPanel("Tags"), 
        FieldPanel("ColorScheme"),
        ImageChooserPanel("Profile_Pic"), 
        PageChooserPanel("Button_Router"),
        FieldPanel('Resume')
    ]
