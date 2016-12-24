# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_remove_tutorial_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='level',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='step',
            name='name',
            field=models.CharField(max_length=250, verbose_name='name', help_text='Please name your step.'),
        ),
    ]
