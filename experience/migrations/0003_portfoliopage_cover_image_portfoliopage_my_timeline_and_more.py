# Generated by Django 4.0.4 on 2022-05-02 20:28

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('experience', '0002_alter_projectpage_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopage',
            name='Cover_Image',
            field=models.ForeignKey(help_text='Background Image for header', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='portfoliopage',
            name='My_Timeline',
            field=wagtail.core.fields.StreamField([('Timeline_Block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100)), ('text', wagtail.core.blocks.TextBlock()), ('date', wagtail.core.blocks.DateBlock())]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='Cover_Image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.image'),
        ),
    ]
