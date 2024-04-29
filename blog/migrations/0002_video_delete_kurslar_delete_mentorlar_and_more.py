# Generated by Django 5.0.4 on 2024-04-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video')),
            ],
        ),
        migrations.DeleteModel(
            name='Kurslar',
        ),
        migrations.DeleteModel(
            name='Mentorlar',
        ),
        migrations.DeleteModel(
            name='Oquvchilar',
        ),
        migrations.DeleteModel(
            name='University',
        ),
        migrations.RemoveField(
            model_name='about',
            name='title',
        ),
        migrations.RemoveField(
            model_name='about',
            name='university',
        ),
        migrations.RemoveField(
            model_name='about',
            name='video',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='description',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='title',
        ),
    ]
