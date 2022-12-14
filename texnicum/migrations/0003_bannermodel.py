# Generated by Django 3.2.6 on 2022-09-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texnicum', '0002_auto_20220929_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='banner')),
                ('title', models.CharField(max_length=555)),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
    ]
