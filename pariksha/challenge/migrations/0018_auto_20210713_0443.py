# Generated by Django 3.0.4 on 2021-07-13 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0017_remove_democodes_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate_codes',
            name='submitted_code_language',
            field=models.TextField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='test_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='challenge.Challenge'),
        ),
    ]
