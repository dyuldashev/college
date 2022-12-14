# Generated by Django 3.2.6 on 2022-09-29 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texnicum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departmentmodels',
            name='short_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documentsofadmissionsmodel',
            name='short_document',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='departmentmodels',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documentsofadmissionsmodel',
            name='documents',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacancymodel',
            name='requirement',
            field=models.TextField(blank=True, null=True),
        ),
    ]
