# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_text',
            field=djangocms_text_ckeditor.fields.HTMLField(help_text='Please provide an answer to this question.'),
        ),
    ]
