# Generated by Django 3.1.2 on 2020-11-05 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0005_focuslist_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='language',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='text.language'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TmpGoogleResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_word', models.CharField(max_length=200)),
                ('rankn', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=2000, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_google', models.DateTimeField(blank=True, null=True, verbose_name='Date Google')),
                ('date_scrap', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Scrapped')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text.domain')),
            ],
            options={
                'db_table': 'tmp_google_result',
            },
        ),
    ]