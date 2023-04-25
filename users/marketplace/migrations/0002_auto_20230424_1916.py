# Generated by Django 3.2 on 2023-04-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]