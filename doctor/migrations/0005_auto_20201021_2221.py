# Generated by Django 2.1.5 on 2020-10-22 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_doctorinfo_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinfo',
            name='doc_id',
            field=models.CharField(max_length=50),
        ),
    ]
