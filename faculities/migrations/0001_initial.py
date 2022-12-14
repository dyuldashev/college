# Generated by Django 3.2.6 on 2022-09-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacultiesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculities', models.CharField(max_length=150)),
                ('information', models.TextField()),
                ('images', models.ImageField(upload_to='faculties')),
            ],
            options={
                'verbose_name': 'faculty',
                'verbose_name_plural': 'faculties',
            },
        ),
    ]
