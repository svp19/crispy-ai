# Generated by Django 2.0.10 on 2019-05-22 03:12

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False
    dependencies = [
        ('ai_admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseModels',
            new_name='CourseModel',
        ),
    ]