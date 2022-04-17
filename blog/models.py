from django.db import models
from django.forms import Field
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
 

# Create your models here.
class BlogListingPage(Page):
    Cover_Image = models.ForeignKey("wagtailimages.Image",blank = False,null = True,related_name = "+",help_text = "Cover Image for the blog page",on_delete = models.SET_NULL)
    Headline_Text = models.CharField(max_length = 70,blank = True,help_text = "Catchy Line for the Blog Page")
    content_panels = Page.content_panels+[
        ImageChooserPanel("Cover_Image"),
        FieldPanel("Headline_Text"),
    ]
class Blog(Page):
    Date_of_Creation = models.DateField("Published Date")
    Title = models.CharField(max_length=500)
    Content = RichTextField(blank = True)
    content_panels = Page.content_panels +[
            FieldPanel("Date_of_Creation"),
            FieldPanel("Title"),
            FieldPanel("Content",classname = "full"),
        ]
    template = "blog/blog_page.html"