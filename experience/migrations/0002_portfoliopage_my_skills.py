# Generated by Django 3.2.13 on 2022-06-22 10:49

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopage',
            name='My_Skills',
            field=wagtail.core.fields.StreamField([('Skill_Block', wagtail.core.blocks.StructBlock([('Skill', wagtail.core.blocks.CharBlock(max_length=100)), ('Percentage', wagtail.core.blocks.IntegerBlock(max_value=100))]))], blank=True, null=True),
        ),
    ]