# Generated by Django 3.2.6 on 2022-09-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texnicum', '0004_auto_20220930_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannermodel',
            name='descriptions',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]