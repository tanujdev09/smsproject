# Generated by Django 5.0.7 on 2024-09-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Register_Number', models.CharField(max_length=10, unique=True)),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
    ]
