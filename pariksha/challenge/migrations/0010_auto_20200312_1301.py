# Generated by Django 3.0 on 2020-03-12 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0009_candidate_count'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='candidate_codes',
            unique_together={('candidate', 'question')},
        ),
    ]
