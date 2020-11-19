# Generated by Django 3.1.2 on 2020-11-04 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0002_appparameters_domain_domainlist_genericsearch_googleresult_language_project_searchresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('ngram', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'word',
            },
        ),
        migrations.CreateModel(
            name='FocusList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('public', models.BooleanField()),
                ('words', models.ManyToManyField(to='text.Word')),
            ],
        ),
    ]