# Generated by Django 3.2.6 on 2022-09-30 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texnicum', '0003_bannermodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bannermodel',
            options={'verbose_name': 'banner', 'verbose_name_plural': 'banners'},
        ),
        migrations.AddField(
            model_name='staffmodel',
            name='short_biography',
            field=models.TextField(blank=True, null=True, verbose_name='short_biography'),
        ),
        migrations.AlterField(
            model_name='bannermodel',
            name='images',
            field=models.ImageField(upload_to='banner', verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='bannermodel',
            name='title',
            field=models.CharField(max_length=555, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='departmentmodels',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='departmentmodels',
            name='images',
            field=models.ImageField(upload_to='department', verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='departmentmodels',
            name='short_content',
            field=models.TextField(blank=True, null=True, verbose_name='short_content'),
        ),
        migrations.AlterField(
            model_name='departmentmodels',
            name='title',
            field=models.CharField(max_length=555, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='documentsofadmissionsmodel',
            name='documents',
            field=models.TextField(blank=True, null=True, verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='documentsofadmissionsmodel',
            name='images',
            field=models.ImageField(upload_to='documents', verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='documentsofadmissionsmodel',
            name='short_document',
            field=models.TextField(blank=True, null=True, verbose_name='short_document'),
        ),
        migrations.AlterField(
            model_name='documentsofadmissionsmodel',
            name='title',
            field=models.CharField(max_length=150, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='biography',
            field=models.TextField(blank=True, null=True, verbose_name='biography'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='images',
            field=models.ImageField(upload_to='staff', verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='position',
            field=models.CharField(max_length=50, verbose_name='position'),
        ),
        migrations.AlterField(
            model_name='vacancymodel',
            name='images',
            field=models.ImageField(upload_to='vacancy', verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='vacancymodel',
            name='positions',
            field=models.CharField(max_length=150, verbose_name='positions'),
        ),
        migrations.AlterField(
            model_name='vacancymodel',
            name='requirement',
            field=models.TextField(blank=True, null=True, verbose_name='requirement'),
        ),
    ]
