# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StreamPreference',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('username', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
    ]
