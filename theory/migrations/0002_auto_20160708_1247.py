# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('theory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='desc',
            field=djangocms_text_ckeditor.fields.HTMLField(help_text='Please describe your attachment.', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=djangocms_text_ckeditor.fields.HTMLField(help_text='Please describe the category.', blank=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='desc',
            field=djangocms_text_ckeditor.fields.HTMLField(help_text='Please describe your tutorial.', blank=True),
        ),
    ]
