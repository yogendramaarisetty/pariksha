# Generated by Django 3.0.4 on 2022-10-12 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0019_submission'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField()),
                ('value', models.BooleanField()),
                ('description', models.TextField()),
            ],
        ),
    ]
