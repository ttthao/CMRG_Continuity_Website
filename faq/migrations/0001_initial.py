# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('category', models.CharField(verbose_name='Category Name', max_length=100, help_text='Please provide a category to group questions together.')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question_text', models.CharField(verbose_name='Frequently Asked Question', max_length=250, help_text='Please provide a frequently asked question.')),
                ('answer_text', models.TextField(help_text='Please provide an answer to this question.')),
                ('category', models.ForeignKey(help_text='Please categorize this question.', to='faq.Category')),
            ],
        ),
    ]
