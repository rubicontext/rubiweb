# Generated by Django 3.1.2 on 2020-11-19 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0018_auto_20201112_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapaction',
            name='domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='text.domain'),
        ),
    ]
