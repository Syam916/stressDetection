# Generated by Django 4.1.7 on 2023-03-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StressDetection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(max_length=10)),
                ('question2', models.CharField(max_length=10)),
                ('question3', models.CharField(max_length=10)),
                ('question4', models.CharField(max_length=10)),
                ('question5', models.CharField(max_length=10)),
                ('question6', models.CharField(max_length=10)),
                ('question7', models.CharField(max_length=10)),
                ('question8', models.CharField(max_length=10)),
                ('question9', models.CharField(max_length=10)),
                ('question10', models.CharField(max_length=10)),
                ('question11', models.CharField(max_length=10)),
                ('question12', models.CharField(max_length=10)),
                ('question13', models.CharField(max_length=10)),
            ],
        ),
    ]
