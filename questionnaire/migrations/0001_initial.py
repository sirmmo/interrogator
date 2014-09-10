# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Done',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DoneAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'ordering': ('question__order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=1000)),
                ('value', models.IntegerField()),
                ('order', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('order', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('min_points', models.IntegerField(default=0)),
                ('max_points', models.IntegerField(default=100)),
                ('text', models.TextField()),
                ('questionnaire', models.ForeignKey(related_name=b'responses', to='questionnaire.Questionnaire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(related_name=b'questions', to='questionnaire.Questionnaire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(to='questionnaire.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doneanswer',
            name='answer',
            field=models.ForeignKey(to='questionnaire.Option'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doneanswer',
            name='done',
            field=models.ForeignKey(related_name=b'answers', to='questionnaire.Done'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doneanswer',
            name='question',
            field=models.ForeignKey(to='questionnaire.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='done',
            name='questionnaire',
            field=models.ForeignKey(related_name=b'answers', to='questionnaire.Questionnaire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='done',
            name='response',
            field=models.ForeignKey(to='questionnaire.Response'),
            preserve_default=True,
        ),
    ]
