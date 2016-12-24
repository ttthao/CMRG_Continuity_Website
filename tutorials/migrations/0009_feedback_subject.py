# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0008_auto_20160714_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='subject',
            field=models.CharField(max_length=100, help_text='Subject of your comment.', default='Subject'),
        ),
    ]
