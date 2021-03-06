# Generated by Django 3.0 on 2020-02-18 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='', max_length=24)),
                ('rollnumber', models.CharField(default='', max_length=20)),
                ('college', models.CharField(default='', max_length=50)),
                ('graduation_year', models.IntegerField(default=0)),
                ('branch', models.CharField(default=0, max_length=50)),
                ('mobile_number', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('submitted_code', models.TextField(max_length=10000)),
                ('total_score', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('resume', models.FileField(default='default.pdf', null=True, upload_to='resumes')),
                ('completed_status', models.BooleanField(default=False)),
                ('suspicious_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Slug', models.SlugField()),
                ('Title', models.CharField(max_length=120)),
                ('Description', models.TextField(max_length=520)),
                ('College', models.CharField(max_length=120)),
                ('Date', models.CharField(default='', max_length=20)),
                ('Test_Duration', models.IntegerField(default=0)),
                ('Active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Slug', models.SlugField()),
                ('Title', models.CharField(max_length=120)),
                ('Type', models.CharField(max_length=120)),
                ('Description', models.TextField(max_length=1000000)),
                ('sample_inputs', models.TextField(max_length=500)),
                ('sample_outputs', models.TextField(max_length=500)),
                ('default_c_code', models.TextField(default='#include<stdio.h>\n\nint main() {\n    \n    printf("");\n    \n}\n', max_length=1000000)),
                ('default_cpp_code', models.TextField(default='#include <iostream>\n\nusing namespace std;\n\nint main() {\n    \n    cout<<"";\n}\n', max_length=1000000)),
                ('default_csharp_code', models.TextField(default='//Note don\'t change the class name \nusing System;\n\nclass Program\n{\n    static void Main() {\n        Console.Write("");\n    }\n}\n', max_length=1000000)),
                ('default_java_code', models.TextField(default='//NOTE: Don\'t change class name\npublic class MyClass {\n    public static void main(String args[]) {\n      System.out.println("" );\n    }\n}\n', max_length=1000000)),
                ('default_python_code', models.TextField(default="if __name__ == '__main__':\n", max_length=1000000)),
                ('challenge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='challenge.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='testcases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input1', models.TextField(default='', max_length=1000000)),
                ('output1', models.TextField(default='', max_length=1000000)),
                ('input2', models.TextField(default='', max_length=1000000)),
                ('output2', models.TextField(default='', max_length=1000000)),
                ('input3', models.TextField(default='', max_length=1000000)),
                ('output3', models.TextField(default='', max_length=1000000)),
                ('input4', models.TextField(default='', max_length=1000000)),
                ('output4', models.TextField(default='', max_length=1000000)),
                ('input5', models.TextField(default='', max_length=1000000)),
                ('output5', models.TextField(default='', max_length=1000000)),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='challenge.Question')),
            ],
        ),
        migrations.CreateModel(
            name='submittedcodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission', models.TextField(max_length=10000)),
                ('score', models.IntegerField(default=0)),
                ('Challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Challenge')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate_codes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_code', models.TextField(default='#include<stdio.h>\n\nint main() {\n    \n    printf("");\n    \n}\n', max_length=1000000)),
                ('cpp_code', models.TextField(default='#include <iostream>\n\nusing namespace std;\n\nint main() {\n    \n    cout<<"";\n}\n', max_length=1000000)),
                ('csharp_code', models.TextField(default='//Note don\'t change the class name \nusing System;\n\nclass Program\n{\n    static void Main() {\n        Console.Write("");\n    }\n}\n', max_length=1000000)),
                ('java_code', models.TextField(default='//NOTE: Don\'t change class name\npublic class MyClass {\n    public static void main(String args[]) {\n      System.out.println("" );\n    }\n}\n', max_length=1000000)),
                ('python_code', models.TextField(default="if __name__ == '__main__':\n", max_length=1000000)),
                ('submitted_code', models.TextField(default='NA', max_length=1000000)),
                ('score', models.IntegerField(default=0)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Candidate')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Question')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='test_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Challenge'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
