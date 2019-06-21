# Generated by Django 2.1.3 on 2019-06-20 17:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('ai_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturemodel',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ai_admin.CourseModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecturemodel',
            name='lecture_id',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecturemodel',
            name='live_transcript',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecturemodel',
            name='summary',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecturemodel',
            name='tags',
            field=models.TextField(null=True),
        ),
    ]
