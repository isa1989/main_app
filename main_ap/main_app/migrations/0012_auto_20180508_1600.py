# Generated by Django 2.0.5 on 2018-05-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20180508_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiccontent',
            name='order',
            field=models.FloatField(default=0),
        ),
    ]
