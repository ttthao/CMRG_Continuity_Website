# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Attachment Name', help_text='Please provide a name for your attachment.', max_length=100)),
                ('desc', djangocms_text_ckeditor.fields.HTMLField(help_text='Please describe your attachment.')),
                ('attachment', models.FileField(help_text='Please provide an attachment.', upload_to='lectures/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Category Name', help_text='Please provide a name for your category.', max_length=100)),
                ('desc', djangocms_text_ckeditor.fields.HTMLField(help_text='Please describe the category.')),
                ('icon', models.ImageField(help_text='Please provide an icon representing the category.', upload_to='theory/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Lecture Name', help_text='Please provide a name for your tutorial.', max_length=100)),
                ('desc', djangocms_text_ckeditor.fields.HTMLField(help_text='Please describe your tutorial.')),
                ('category', models.ForeignKey(help_text='Please categorize your lecture.', to='theory.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Reading Name', help_text='Please provide a name for your reading.', max_length=300)),
                ('attachment', models.FileField(help_text='Please provide an attachment.', upload_to='reading/', blank=True)),
                ('category', models.ForeignKey(help_text='Please categorize your reading to a category.', to='theory.Category')),
            ],
        ),
        migrations.AddField(
            model_name='attachment',
            name='lecture',
            field=models.ForeignKey(help_text='Please indicate which lecture this attachment is for.', to='theory.Lecture'),
        ),
    ]
