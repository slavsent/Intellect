# Generated by Django 4.2.7 on 2023-11-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='time_quote',
            field=models.DateTimeField(verbose_name='Time'),
        ),
    ]
