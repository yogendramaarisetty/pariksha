# Generated by Django 3.0 on 2020-02-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0005_auto_20200228_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='sample_inputs',
        ),
        migrations.RemoveField(
            model_name='question',
            name='sample_outputs',
        ),
        migrations.AlterField(
            model_name='question',
            name='Description',
            field=models.TextField(),
        ),
    ]
