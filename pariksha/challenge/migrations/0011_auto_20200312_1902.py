# Generated by Django 3.0 on 2020-03-12 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0010_auto_20200312_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge_questions',
            name='challenge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='challenge.Challenge'),
        ),
        migrations.AlterField(
            model_name='challenge_questions',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='challenge.Question'),
        ),
    ]
