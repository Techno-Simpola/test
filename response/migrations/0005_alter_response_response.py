# Generated by Django 4.0.2 on 2022-02-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0004_auto_20210308_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='response',
            field=models.CharField(max_length=500),
        ),
    ]
