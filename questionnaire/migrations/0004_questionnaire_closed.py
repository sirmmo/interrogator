# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_auto_20140910_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='closed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
