# Generated by Django 5.1 on 2024-08-31 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, null=True)),
                ('answer1', models.CharField(max_length=255, null=True)),
                ('answer2', models.CharField(max_length=255, null=True)),
                ('answer3', models.CharField(max_length=255, null=True)),
                ('answer4', models.CharField(max_length=255, null=True)),
                ('correct_answer', models.IntegerField(null=True)),
                ('points', models.IntegerField(null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
