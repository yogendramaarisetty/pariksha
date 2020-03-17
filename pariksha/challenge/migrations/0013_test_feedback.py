# Generated by Django 3.0 on 2020-03-16 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0012_auto_20200315_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, max_length=5)),
                ('description', models.TextField(default='')),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Candidate')),
            ],
        ),
    ]