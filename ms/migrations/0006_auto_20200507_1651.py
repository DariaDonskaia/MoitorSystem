# Generated by Django 2.2.12 on 2020-05-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms', '0005_auto_20200507_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gateway',
            name='gateway_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
