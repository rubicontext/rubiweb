# Generated by Django 3.1.2 on 2020-11-05 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0008_auto_20201105_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]