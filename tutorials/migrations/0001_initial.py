# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Category Name', help_text='Please provide a name for your category.', max_length=100)),
                ('desc', djangocms_text_ckeditor.fields.HTMLField(help_text='Please describe the category.')),
                ('icon', models.ImageField(help_text='Please provide an icon representing the category.', upload_to='tutorials', default='#', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='name', help_text='Please name your step.', max_length='250')),
                ('step', cms.models.fields.PlaceholderField(null=True, to='cms.Placeholder', slotname='step', editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Tutorial Name', help_text='Please provide a name for your tutorial.', max_length=100)),
                ('desc', djangocms_text_ckeditor.fields.HTMLField(help_text='Please describe your tutorial.')),
                ('level', models.PositiveSmallIntegerField(default=1)),
                ('category', models.ForeignKey(to='tutorials.Category', help_text='Please categorize your tutorial.')),
            ],
        ),
        migrations.AddField(
            model_name='step',
            name='tutorial',
            field=models.ForeignKey(to='tutorials.Tutorial', help_text='Please place your step in a tutorial.'),
        ),
    ]
