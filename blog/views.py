from django.shortcuts import render,HttpResponseRedirect
from blog.models import *
import hashlib
from pymysql import connect


def setPassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result

def loginValid(fun):
    def inner(request,*args,**kwargs):
        cookie = request.COOKIES.get('email')
        if cookie :
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/login/')
    return inner

def base(request):
    cookie = request.COOKIES.get('email')
    if request.method == 'POST':
        x = request.POST.get('search_text')
        booklist = Tushu.objects.filter(title=f'select * from blog_tushu where title like "{x}"')
        return render(request,'book_list.html',locals())
    return render(request,'base.html',locals())

def index(request):
    cookie = request.COOKIES.get('email')
    if cookie:
        cookie = User.objects.get(email=cookie)
    book_list = Tushu.objects.all().order_by('-press_year')[:10]
    type_list = Types.objects.all()[:22]
    booke = Tushu.objects.all()[:10]
    return render(request,'index.html',locals())
def details(request,id):
    cookie = request.COOKIES.get('email')
    cookie = User.objects.get(email=cookie)
    book_list = Tushu.objects.filter(id=id)
    type_list = Tushu.objects.filter(types=[book.types for book in book_list][0])[:10]
    return render(request,'details.html',locals())
def login(request):

    if request.method=='POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()
        if user:
            from_password=setPassword(password)
            db_password = user.password
            if from_password == db_password:
                response = HttpResponseRedirect('/')
                response.set_cookie('email',user.email)

                return response
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        nickname = request.POST.get('nickname')
        email = request.POST.get('username')
        password = request.POST.get('password')
        user =User()
        user.nickname = nickname
        user.email = email
        user.password = setPassword(password)
        user.verification_code = '暂无'
        user.save()
        return HttpResponseRedirect('/login/')
    return render(request,'register.html')
# Create your views here.


def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('email')
    return response
def book_list(request,types,page):
    cookie = request.COOKIES.get('email')
    cookie = User.objects.get(email=cookie)
    page_int = int(page)
    start = (page_int-1)*10
    end = page_int*10
    if types=='新书':
        booklist = Tushu.objects.all().order_by('-press_year')[:20]
    elif types=='高评分榜单':
        booklist = Tushu.objects.all().order_by('-score')[:20]
    elif types=='全部':
        booklist = Tushu.objects.all()[start:end]
        if page_int<3:
            page_range = range(1,6)
        else:
            page_range = range(page_int - 2, page_int + 3)
    elif types =='日期':
        booklist = Tushu.objects.all().order_by('-press_year')
        if page_int<3:
            page_range = range(1,6)
        else:
            page_range = range(page_int - 2, page_int + 3)
    else:
        booklist = Tushu.objects.filter(types=types)

    return render(request,'book_list.html',locals())
