# Generated by Django 2.1.5 on 2020-10-22 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_auto_20201022_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinfo',
            name='birthday',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='education_year',
            field=models.DateTimeField(),
        ),
    ]
