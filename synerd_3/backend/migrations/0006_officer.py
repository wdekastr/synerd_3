# Generated by Django 2.1.7 on 2019-04-11 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_transferredsubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('officecode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Office')),
                ('subscriberID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Subscriber')),
            ],
        ),
    ]
