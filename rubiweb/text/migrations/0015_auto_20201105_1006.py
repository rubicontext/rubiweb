# Generated by Django 3.1.2 on 2020-11-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0014_auto_20201105_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectsearch',
            name='exact_expression',
        ),
        migrations.AddField(
            model_name='genericsearch',
            name='exact_expression',
            field=models.BooleanField(default=False),
        ),
    ]
