from django.db import models
from wagtail.contrib.settings.models import BaseSetting,register_setting
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
# Create your models here.
@register_setting
class DynamicSettings(BaseSetting):
    class Meta:
        verbose_name = "Site Configurations"
    Site_Name = models.CharField(max_length = 500,help_text = "Name of the Site")
    Site_Logo = models.ForeignKey(
        'wagtailimages.Image',blank = True, null = True, on_delete = models.SET_NULL
    )
    panels = [
        FieldPanel('Site_Name'),
        ImageChooserPanel('Site_Logo')
    ]
@register_setting
class SocialMediaSettings(BaseSetting):
    class Meta:
        verbose_name = 'Social Media Accounts'
    LinkedIn = models.URLField(help_text = "LinkedIn Page URL")
    Email = models.EmailField(help_text = "Email")
    Twitter = models.URLField(help_text = "Twitter Page URL",blank = True)
    GitHub = models.URLField(help_text = "GitHub URL")
    Discord = models.URLField(help_text = "Discord ID")
    
    panels = [
        FieldPanel("LinkedIn"),
        FieldPanel("Email"),
        FieldPanel("GitHub"),
        FieldPanel("Twitter"),
        FieldPanel("Discord"),
    ]