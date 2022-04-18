from django.db import models
from django.forms import Field
from wagtail.core import blocks
from wagtailblocks.models import ResponsiveImageBlock,CardBlock
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

# Create your models here.
class BlogListingPage(Page):
    Cover_Image = models.ForeignKey("wagtailimages.Image",blank = False,null = True,related_name = "+",help_text = "Cover Image for the blog page",on_delete = models.SET_NULL)
    Headline_Text = models.CharField(max_length = 70,blank = True,help_text = "Catchy Line for the Blog Page")
    content_panels = Page.content_panels+[
        ImageChooserPanel("Cover_Image"),
        FieldPanel("Headline_Text"),
    ]
    subpage_types = ['blog.Blog']
    def get_context(self,request):
        context = super().get_context(request)
        Blogs = self.get_children().live().order_by('-first_published_at')
        context['Blogs'] = Blogs
        return context
class Blog(Page):
    Date_of_Creation = models.DateField("Published Date")
    Title = models.CharField(max_length=500)
    Content = StreamField([
        ('heading',blocks.CharBlock(classname = "Full Title")),
        ('paragraph',blocks.RichTextBlock()),
        ('responsive_image',ResponsiveImageBlock()),
        ('card',CardBlock()),
        ('image',ImageChooserBlock()),
        ],blank = True
    )
    content_panels = Page.content_panels +[
            FieldPanel("Date_of_Creation"),
            FieldPanel("Title"),
            StreamFieldPanel("Content",classname = "full"),
        ]
    template = "blog/blog_page.html"
    