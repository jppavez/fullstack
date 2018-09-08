# Generated by Django 2.0.5 on 2018-09-08 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='stock_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
