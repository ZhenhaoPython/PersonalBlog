# Generated by Django 2.2.1 on 2019-07-18 17:25

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190718_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='article',
            field=models.ForeignKey(on_delete=blog.models.Tushu, to='blog.Tushu'),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]