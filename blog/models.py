from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32,unique=True,verbose_name='账号')
    password = models.CharField(max_length=16,verbose_name='登录密码')
    nickname = models.CharField(default='暂无',verbose_name='昵称',max_length=32)
    email = models.CharField(max_length=32)
    verification_code = models.CharField(verbose_name='邮箱验证码',null=True,max_length=32)
    head_portrait = models.ImageField(upload_to='images',default='/images/moren.jpg')
class Types(models.Model):
    label = models.CharField(max_length=32)
class Tushu(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    press = models.CharField(max_length=32)
    press_year = models.CharField(max_length=32)
    page = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    binding = models.CharField(max_length=32)
    series = models.CharField(max_length=32)
    score = models.CharField(max_length=32)
    content = models.TextField()
    imtroducyion = models.TextField()
    types = models.CharField(max_length=32)
    img = models.CharField(max_length=64)
class Message(models.Model):
    name = models.ForeignKey('User',on_delete=True)
    data = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=False)
    article = models.ForeignKey('Tushu',on_delete=True)