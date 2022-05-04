from django.db import models
from wagtailblocks.models import TimelineBlock
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.core.fields import RichTextField, StreamField
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel,MultiFieldPanel
# Create your models here.
class PortfolioPage(Page):
    Cover_Image = models.ForeignKey('wagtailimages.Image',blank = False,null = True,on_delete = models.SET_NULL,help_text = "Background Image for header")
    
    My_Timeline = StreamField([
        ("Timeline_Block", TimelineBlock()),
    ], null=True, blank=True)
    content_panels = Page.content_panels+[
        ImageChooserPanel('Cover_Image'),
        StreamFieldPanel('My_Timeline')
    ]
    def get_context(self, request):
        context = super().get_context(request)
        project_pages = self.get_children().live().order_by('-first_published_at')
        context['project_pages'] = project_pages
        return context
    template = "experience/portfolio_page.html"
class ProjectPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'Project',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )
class Project(Page):
    Date_of_Creation = models.DateField("Published Date")
    Description = RichTextField()
    Cover_Image = models.ForeignKey('wagtailimages.Image',blank = True,null = True,on_delete = models.SET_NULL)
    Softwares_Used = ClusterTaggableManager(through=ProjectPageTag, blank=True)
    content_panels = Page.content_panels+[
        FieldPanel('Date_of_Creation'),
        FieldPanel('Description'),
        ImageChooserPanel('Cover_Image'),
    ]
