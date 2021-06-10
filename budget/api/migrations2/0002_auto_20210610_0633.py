# Generated by Django 3.2.4 on 2021-06-10 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='startdate',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата начала действия записи'),
        ),
        migrations.AlterUniqueTogether(
            name='budget',
            unique_together={('code', 'name')},
        ),
    ]