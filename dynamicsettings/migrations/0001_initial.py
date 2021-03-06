# Generated by Django 3.2.13 on 2022-05-05 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LinkedIn', models.URLField(help_text='LinkedIn Page URL')),
                ('Email', models.EmailField(help_text='Email', max_length=254)),
                ('Twitter', models.URLField(blank=True, help_text='Twitter Page URL')),
                ('GitHub', models.URLField(help_text='GitHub URL')),
                ('Discord', models.URLField(help_text='Discord ID')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Social Media Accounts',
            },
        ),
        migrations.CreateModel(
            name='DynamicSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Site_Name', models.CharField(help_text='Name of the Site', max_length=500)),
                ('Site_Logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.image')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Site Configurations',
            },
        ),
    ]
