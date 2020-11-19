# Generated by Django 3.1.2 on 2020-11-05 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0006_auto_20201105_0404'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('daily_limit', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'external_api',
            },
        ),
        migrations.AlterModelTable(
            name='focuslist',
            table='focus_list',
        ),
        migrations.CreateModel(
            name='ScrapAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_word', models.CharField(max_length=200)),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date creation')),
                ('date_modification', models.DateTimeField(auto_now=True, null=True, verbose_name='Date modification')),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('nb_results', models.IntegerField(blank=True, null=True)),
                ('nb_duplicates', models.IntegerField(blank=True, null=True)),
                ('nb_existing_other_searches', models.IntegerField(blank=True, null=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text.domain')),
            ],
            options={
                'db_table': 'scrap_action',
            },
        ),
        migrations.CreateModel(
            name='ExternalAPIUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date creation')),
                ('nb_calls', models.IntegerField(blank=True, null=True)),
                ('external_api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text.externalapi')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text.project')),
            ],
            options={
                'db_table': 'external_api_usage',
            },
        ),
        migrations.CreateModel(
            name='ExternalAPIProjectQuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_limit', models.IntegerField(blank=True, null=True)),
                ('external_api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text.externalapi')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text.project')),
            ],
            options={
                'db_table': 'external_api_project_quota',
            },
        ),
    ]
