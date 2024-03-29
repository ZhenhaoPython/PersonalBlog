# Generated by Django 2.2.1 on 2019-07-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tushu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('author', models.CharField(max_length=32)),
                ('press', models.CharField(max_length=32)),
                ('press_year', models.CharField(max_length=32)),
                ('page', models.CharField(max_length=32)),
                ('price', models.CharField(max_length=32)),
                ('binding', models.CharField(max_length=32)),
                ('series', models.CharField(max_length=32)),
                ('score', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('imtroducyion', models.TextField()),
                ('types', models.CharField(max_length=32)),
                ('img', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='账号')),
                ('password', models.CharField(max_length=16, verbose_name='登录密码')),
                ('nickname', models.CharField(default='暂无', max_length=32, verbose_name='昵称')),
                ('email', models.CharField(max_length=32)),
                ('verification_code', models.CharField(max_length=32, null=True, verbose_name='邮箱验证码')),
                ('head_portrait', models.ImageField(default='/images/moren.jpg', upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('article', models.ForeignKey(on_delete=True, to='blog.Tushu')),
                ('name', models.ForeignKey(on_delete=True, to='blog.User')),
            ],
        ),
    ]
