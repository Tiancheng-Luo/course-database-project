# Generated by Django 2.0.2 on 2018-04-26 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseSite', '0008_course_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ratings',
            field=models.IntegerField(null=True),
        ),
    ]
