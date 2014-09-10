# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_auto_20140910_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='description',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='header_template',
            field=models.TextField(default=b''),
        ),
    ]
