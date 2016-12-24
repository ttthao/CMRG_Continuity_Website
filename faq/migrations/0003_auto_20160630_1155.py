# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_auto_20160623_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(help_text='Please provide a frequently asked question.', verbose_name='Frequently Asked Question', max_length=350),
        ),
    ]
