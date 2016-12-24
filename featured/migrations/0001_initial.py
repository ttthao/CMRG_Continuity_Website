# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import djangocms_text_ckeditor.fields
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('header', models.CharField(max_length=200, verbose_name='Featured Story Header', help_text='Please provide a header for your story.')),
                ('date', models.DateField(default=datetime.date.today, help_text='Please specify when this story was written.')),
                ('image', models.ImageField(upload_to='featured', help_text='Please provide an image to go with your story.')),
                ('snippet', djangocms_text_ckeditor.fields.HTMLField(help_text='Please provide a SHORT snippet of the story.')),
                ('details', cms.models.fields.PlaceholderField(editable=False, slotname='details', to='cms.Placeholder', null=True)),
            ],
        ),
    ]
