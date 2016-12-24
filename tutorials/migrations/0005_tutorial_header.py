# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0004_auto_20160627_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='header',
            field=models.CharField(verbose_name='Tutorial Header', max_length=200, blank=True, help_text='Please provide a SHORT description for your tutorial.'),
        ),
    ]
