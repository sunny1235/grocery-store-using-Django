# Generated by Django 3.0.6 on 2020-08-22 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_bestservingproduct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BestServingProduct',
        ),
        migrations.DeleteModel(
            name='homePageslides',
        ),
        migrations.DeleteModel(
            name='product',
        ),
    ]
