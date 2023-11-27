# Generated by Django 4.2.5 on 2023-11-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cartdetail',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
