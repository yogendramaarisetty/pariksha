# Generated by Django 3.0 on 2020-02-20 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='challenge',
        ),
        migrations.CreateModel(
            name='challenge_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='challenge.Question')),
                ('challenge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='challenge.Challenge')),
            ],
        ),
    ]
