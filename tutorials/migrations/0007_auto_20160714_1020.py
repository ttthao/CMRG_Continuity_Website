# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0006_auto_20160630_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('rating', models.PositiveSmallIntegerField(verbose_name='Rating', help_text='User rating.', max_length=5)),
                ('comment', models.TextField(help_text='User comments.')),
            ],
        ),
        migrations.AddField(
            model_name='tutorial',
            name='author',
            field=models.CharField(default='Anonymous', verbose_name='Author Name', help_text='Please provide your name.', max_length=100),
        ),
        migrations.AddField(
            model_name='feedback',
            name='tutorial',
            field=models.ForeignKey(help_text='Please associate your feedback with a tutorial.', to='tutorials.Tutorial'),
        ),
    ]
