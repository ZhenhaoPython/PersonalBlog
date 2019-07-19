from django.db import models

# Create your models here.
class User(models.Model):
    password = models.CharField(max_length=64,verbose_name='登录密码')
    nickname = models.CharField(default='暂无',verbose_name='昵称',max_length=32)
    email = models.CharField(max_length=32,unique=True)
    verification_code = models.CharField(verbose_name='邮箱验证码',null=True,max_length=32)
    head_portrait = models.ImageField(upload_to='images',default='images/moren.jpg')
    xingming = models.CharField(max_length=32,default='姓名')
    age = models.CharField(max_length=32,default='年龄')
    work = models.CharField(max_length=32,default='工作')
    tel = models.CharField(max_length=32,default='电话')
    address = models.TextField(default='地址')
class Types(models.Model):
    label = models.CharField(max_length=32)
class Tushu(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    press = models.CharField(max_length=64)
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
    reading_num = models.CharField(max_length=32,default='0')
    comments_num = models.CharField(max_length=32,default='0')
class Message(models.Model):
    name = models.CharField(max_length=32)
    data = models.DateField(auto_now_add=True)
    contents = models.TextField(null=False)
    article = models.ForeignKey('Tushu',on_delete=True)
class Read(models.Model):
    articles = models.ForeignKey('Tushu',on_delete=True)
    name = models.CharField(max_length=32)
    data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images',default='/images/moren.jpg')