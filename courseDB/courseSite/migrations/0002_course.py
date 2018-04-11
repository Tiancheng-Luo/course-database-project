# Generated by Django 2.0.2 on 2018-04-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseSite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10)),
                ('full_title', models.CharField(max_length=250)),
                ('course_number', models.IntegerField()),
                ('department', models.CharField(max_length=5)),
                ('description', models.TextField()),
                ('instructor', models.CharField(max_length=150)),
                ('days', models.CharField(max_length=5)),
                ('times', models.CharField(max_length=10)),
            ],
        ),
    ]
