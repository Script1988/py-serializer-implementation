# Generated by Django 4.1 on 2022-12-18 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='problem_description',
            field=models.TextField(null=True),
        ),
    ]