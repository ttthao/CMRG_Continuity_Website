# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0007_auto_20160714_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.PositiveSmallIntegerField(help_text='User rating.', verbose_name='Rating'),
        ),
    ]
