# Generated by Django 3.0.2 on 2020-04-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20200424_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='img_file',
            field=models.ImageField(null=True, upload_to='images/cat/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='courses',
            name='img_file',
            field=models.ImageField(null=True, upload_to='images/course/', verbose_name=''),
        ),
    ]