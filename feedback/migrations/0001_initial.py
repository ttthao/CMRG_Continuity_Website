# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('category', models.CharField(choices=[('Suggestion/Comments', 'Suggestion/Comments'), ('Bug Report', 'Bug Report')], verbose_name='Category Name', max_length=100)),
                ('subject', models.CharField(choices=[('Continuity', 'Continuity'), ('Blender', 'Blender'), ('Site', 'Site')], verbose_name='Subject Name', max_length=100)),
                ('desc', djangocms_text_ckeditor.fields.HTMLField()),
            ],
        ),
    ]
