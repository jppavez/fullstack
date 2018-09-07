# Generated by Django 2.0.5 on 2018-09-07 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('thumbnail', models.URLField()),
                ('price', models.FloatField()),
                ('upc', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('stock', models.BooleanField(default=False)),
                ('stock_quantity', models.IntegerField()),
            ],
        ),
    ]