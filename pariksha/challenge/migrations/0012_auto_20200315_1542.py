# Generated by Django 3.0 on 2020-03-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0011_auto_20200312_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='Slug',
        ),
        migrations.AddField(
            model_name='question',
            name='Level',
            field=models.CharField(default='easy', max_length=120),
        ),
    ]