# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='header_template',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='done',
            name='response',
            field=models.ForeignKey(blank=True, to='questionnaire.Response', null=True),
        ),
        migrations.AlterField(
            model_name='option',
            name='question',
            field=models.ForeignKey(related_name=b'options', to='questionnaire.Question'),
        ),
    ]
