# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0005_tutorial_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='end',
            field=models.PositiveIntegerField(blank=True, default=1, help_text='OPTIONAL: Please provide an end time for the video, in seconds.'),
        ),
        migrations.AddField(
            model_name='step',
            name='start',
            field=models.IntegerField(blank=True, default=1, help_text='OPTIONAL: Please provide a start time for the video, in seconds.'),
        ),
        migrations.AddField(
            model_name='step',
            name='youtube',
            field=models.URLField(blank=True, help_text='OPTIONAL: Please provide the URL to EMBEDDED YouTube video (not the regular URL).'),
        ),
    ]
