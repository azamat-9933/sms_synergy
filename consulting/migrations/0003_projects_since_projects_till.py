# Generated by Django 5.1.4 on 2024-12-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0002_teammember_delete_photoreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='since',
            field=models.DateField(default='2024-12-08', verbose_name='Since'),
        ),
        migrations.AddField(
            model_name='projects',
            name='till',
            field=models.DateField(default='2024-12-08', verbose_name='Till'),
        ),
    ]
