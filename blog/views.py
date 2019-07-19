from django.shortcuts import render,HttpResponseRedirect
from blog.models import *
import hashlib,time,re
from django.http import JsonResponse


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
    return render(request,'base.html',locals())

def index(request):
    cookie = request.COOKIES.get('email')
    if cookie:
        cookie = User.objects.get(email=cookie)
    book_list = Tushu.objects.order_by('-press_year')[:10]
    type_list = Types.objects.all()[:22]
    booke = Tushu.objects.all()[:10]
    return render(request,'index.html',locals())
def details(request,id):
    cookie = request.COOKIES.get('email')
    if cookie:
        cookie = User.objects.get(email=cookie)
        tushu = Tushu.objects.get(id=id)
        tushu.reading_num = str(int(tushu.reading_num)+1)
        tushu.save()
        read = Read()
        read.articles_id = id
        read.name = cookie.nickname
        read.data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        read.image = cookie.head_portrait
        read.save()
    if request.method == 'POST':
        if cookie:
            content = request.POST.get('pinglun')
            nickname = cookie.nickname
            message = Message()
            message.data =time.strftime('%Y-%m-%d', time.localtime(time.time()))
            message.contents = content
            message.article_id = id
            message.name = nickname
            message.save()
            tushu = Tushu.objects.get(id=id)
            tushu.comments_num = str(int(tushu.comments_num)+1)
            tushu.save()
        else:
            return HttpResponseRedirect('/login/')
    book_list = Tushu.objects.get(id=id)
    type_list = Tushu.objects.filter(types=book_list.types)[:10]
    message_list = Tushu.objects.get(id=id).message_set.order_by('-data')
    reading_list = Tushu.objects.get(id=id).read_set.order_by('-data')[:5]
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
    if cookie:
        cookie = User.objects.get(email=cookie)
    page_int = int(page)
    start = (page_int-1)*10
    end = page_int*10
    if types=='新书':
        booklist = Tushu.objects.all().order_by('-press_year')[:20]
    elif types=='高评分榜单':
        booklist = Tushu.objects.all().order_by('-score')[:10]
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
    elif types =='评分':
        booklist = Tushu.objects.all().order_by('-score')[start:end]
        if page_int < 3:
            page_range = range(1, 6)
        else:
            page_range = range(page_int - 2, page_int + 3)
    else:
        booklist = Tushu.objects.filter(types=types)

    return render(request,'book_list.html',locals())

def prefack_home(request,id):
    cookie = request.COOKIES.get('email')

    cookie = User.objects.get(email=cookie)
    if request.method=='POST':
        nickname = request.POST.get('nickname')
        xingming = request.POST.get('xingming')
        age = request.POST.get('age')
        work = request.POST.get('work')
        tel = request.POST.get('tel')
        address = request.POST.get('address')
        img = request.FILES.get('img')
        user = User.objects.get(id=id)
        user.nickname=nickname
        user.xingming=xingming
        user.age=age
        user.work=work
        user.tel=tel
        user.address=address
        user.head_portrait=img
        user.save()
    user_list = User.objects.get(id=id)
    return render(request,'personal_home.html',locals())
def ajax_data(request):
    result = {'data':'error'}
    if request.method =='POST':
        img = request.FILES.get('img')
        user = User.objects.get(id=1)
        user.head_portrait=img
        user.save()
        result['data']='ok'
    return JsonResponse(result)


def search(request,types):
    title = str(request.POST.get('search_text'))
    search_list = Tushu.objects.all().order_by('-press_year')
    booklist = []
    for book in search_list:
        ok = re.findall(r'.*'+title+'.*',book.title)
        if ok:
            booklist.append(book)
    if booklist == []:
        types='很抱歉客官 暂无此书 -_- 请给我留言 我会尽快添加'
    return render(request,'book_list.html',locals())