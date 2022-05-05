from django.db import models
from django.forms import Field
from wagtail.core import blocks
from wagtail.search import index
from wagtailblocks.models import ResponsiveImageBlock,CardBlock,CustomCodeBlock
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel,MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from wagtailcodeblock.blocks import CodeBlock
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
class BlogPageTag(TaggedItemBase):
	content_object = ParentalKey(
		'Blog',
		related_name='tagged_items',
		on_delete=models.CASCADE
	)
class Blog(Page):
    Date_of_Creation = models.DateField("Published Date")
    Summary = models.CharField(max_length = 500,default = "Hey this is dummy blog text")
    Cover_Image = models.ForeignKey("wagtailimages.Image",blank = False,null = True,on_delete=models.SET_NULL)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    Content = StreamField([
        ('heading',blocks.CharBlock(classname = "Full Title")),
        ('paragraph',blocks.RichTextBlock()),
        ('responsive_image',ResponsiveImageBlock()),
        ('card',CardBlock()),
        ('image',ImageChooserBlock()),
        ('code',CustomCodeBlock()),
        ],
    )
    parent_page_types = ['blog.BlogListingPage']
    search_fields = Page.search_fields + [
		index.SearchField('Summary'),
		index.SearchField('Content'),
	]
    content_panels = Page.content_panels +[
        MultiFieldPanel([
			FieldPanel('Date_of_Creation'),
			FieldPanel('Summary'),
			ImageChooserPanel('Cover_Image'),
			FieldPanel('tags'),
			FieldPanel('owner')
		], heading="Blog Info"),
            StreamFieldPanel("Content",classname = "full"),
        ]
    template = "blog/blog_page.html"
    