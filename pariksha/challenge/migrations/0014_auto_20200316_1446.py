# Generated by Django 3.0 on 2020-03-16 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0013_test_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_feedback',
            name='Candidate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='challenge.Candidate'),
        ),
    ]
