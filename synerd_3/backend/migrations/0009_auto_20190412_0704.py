# Generated by Django 2.1.7 on 2019-04-12 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20190412_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='allocation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
