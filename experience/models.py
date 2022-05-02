from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.
class PortfolioPage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        project_pages = self.get_children().live().order_by('-first_published_at')
        context['project_pages'] = project_pages
        return context
class ProjectPage(Page):
    Date_of_Creation = models.DateField("Published Date")
    Description = RichTextField()
    Cover_Image = models.ForeignKey('wagtailimages.Image',blank = True,null = True,on_delete = models.SET_NULL)
    content_panels = Page.content_panels+[
        FieldPanel('Date_of_Creation'),
        FieldPanel('Description'),
        ImageChooserPanel('Cover_Image'),
    ]
    