# Generated by Django 4.0.4 on 2022-05-05 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule', '0002_alter_timetable_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='date',
            field=models.DateField(verbose_name='Дата пары'),
        ),
    ]
