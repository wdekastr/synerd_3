# Generated by Django 2.1.7 on 2019-04-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_auto_20190412_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='enddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='motifofcancellation',
            field=models.TextField(blank=True, null=True),
        ),
    ]