# Generated by Django 2.2.3 on 2019-12-31 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ee_control_find', '0003_auto_20191231_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedcv',
            name='employee',
            field=models.CharField(max_length=150),
        ),
    ]
