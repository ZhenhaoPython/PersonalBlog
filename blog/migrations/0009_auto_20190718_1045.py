# Generated by Django 2.2.1 on 2019-07-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190718_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
    ]