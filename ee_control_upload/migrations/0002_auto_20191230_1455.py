# Generated by Django 2.2.3 on 2019-12-30 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ee_control_upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='media'),
        ),
    ]
