# Generated by Django 2.1.7 on 2019-04-12 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20190412_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='attribution',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]