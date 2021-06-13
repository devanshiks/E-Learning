# Generated by Django 3.0.2 on 2020-04-24 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='img_file',
            field=models.ImageField(null=True, upload_to='images/cat', verbose_name=''),
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('cname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('img_file', models.ImageField(null=True, upload_to='images/course', verbose_name='')),
                ('user_count', models.IntegerField()),
                ('categoryname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.categories')),
            ],
        ),
    ]
