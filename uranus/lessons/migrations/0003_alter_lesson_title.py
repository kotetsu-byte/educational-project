# Generated by Django 5.1 on 2024-10-19 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_alter_lesson_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
