# Generated by Django 2.2.1 on 2019-07-18 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190718_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='tushu',
            name='comments_num',
            field=models.CharField(default='0', max_length=32),
        ),
        migrations.AddField(
            model_name='tushu',
            name='reading_num',
            field=models.CharField(default='0', max_length=32),
        ),
        migrations.AlterField(
            model_name='message',
            name='article',
            field=models.ForeignKey(on_delete=True, to='blog.Tushu'),
        ),
        migrations.CreateModel(
            name='Read',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('articles', models.ForeignKey(on_delete=True, to='blog.Tushu')),
            ],
        ),
    ]
