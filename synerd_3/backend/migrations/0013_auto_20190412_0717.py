# Generated by Django 2.1.7 on 2019-04-12 07:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20190412_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='address2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='datejoined',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='zipcode',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
