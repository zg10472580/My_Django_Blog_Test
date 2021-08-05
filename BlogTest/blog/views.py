from django.shortcuts import render, get_object_or_404 , HttpResponse
from BlogTest.util import PageInfo
from blog.models import Article , Category , Tag , UserSheet
import base64
import markdown
from datetime import datetime,timedelta
from Crypto.Cipher import AES

# from django.core import serializers#QuerySet类型数据转json ，也就是查询结果转json
from django.db.models import Q

def index(request):
    page_info = GeiBlogTiezo(request)
    inc = Article.objects.all()
    _blog_list = inc[page_info.index_start: page_info.index_end]
    return render(request, 'blog/pai_hang.html', {"blog_list" : _blog_list ,"ab_title" : "主页",
                                                  "ndex_title": {
                                                        "iso": "el-certificate",
                                                        "ins": len(inc)
                                                    }})
def Ret_author(request , name):
    """
    返回作者发的贴子
    :param request:
    :param name:
    :return:
    """
    page_number = get_page(request)
    blog_count = Article.objects.filter(author__username=name)
    page_info = PageInfo(page_number, blog_count.count())

    return render(request, 'blog/pai_hang.html', {
                          "blog_list": blog_count[page_info.index_start: page_info.index_end],
                          "ab_title": "用户:" + name + "发的帖子",
                          "ndex_title": {"ins":blog_count.count(),'iso' : "el-user"}
                        }
                  )

def get_page(request):
    page_number = request.GET.get("page")
    return 1 if not page_number or not page_number.isdigit() else int(page_number)


def category(request, name):
    """
    分类
    :param request:
    :param name:
    :return:
    """
    page_number = get_page(request)
    blog_count = Article.objects.filter(category__name=name)
    page_info = PageInfo(page_number, blog_count.count())

    return render(request, 'blog/pai_hang.html', {
                          "blog_list": blog_count[page_info.index_start: page_info.index_end],
                          "ab_title": "分类",
                          "ndex_title": {"name" : name , "ins":blog_count.count(),'iso' : "el-th-list"}
                        }
                  )

def Search_Index(request):
    key = request.GET.get("name")
    result = Article.objects.filter(Q(title__icontains=key)|Q(digest__icontains=key))
    return render(request, 'blog/pai_hang.html', {
        "ab_title": "搜索",
        "blog_list" : result,
        "ndex_title": {'iso': "el-search","iso2" : key,"name":key,"ins":result.count()}
    }
                  )


def Get_Fenlei(request):
    ty = request.GET.get("tp")
    if ty == "Tag":
        ct = Tag.objects.all()
    elif ty == "Fenlei":
        ct = Category.objects.all()
    t = ''
    for d in ct:
        t += str(d) + "||"
    # a = serializers.serialize("json" , Category.objects.all())
    return HttpResponse(str(t))


def Ret_Tag(request,name):
    """
    返回标签的内容
    :param request:
    :param name:
    :return:
    """

    page_number = get_page(request)
    blog_count = Article.objects.filter(tag__tag_name=name)
    page_info = PageInfo(page_number, blog_count.count())
    return render(request, 'blog/pai_hang.html', {
                          "blog_list": blog_count[page_info.index_start: page_info.index_end],
                          "ab_title": "标签",
                          "ndex_title": {"name" : name , "ins":blog_count.count(),'iso' : "el-tag"}
                        }
                  )

def archive(request):
    #归档    降序
    _blog_list = Article.objects.values("id", "title", "date_time").order_by('-date_time')
    archive_dict = {}
    for blog in _blog_list:
        pub_month = blog.get("date_time").strftime("%Y年%m月")
        if pub_month in archive_dict:
            archive_dict[pub_month].append(blog)
        else:
            archive_dict[pub_month] = [blog]
    data = sorted([{"date": _[0], "blogs": _[1]} for _ in archive_dict.items()], key=lambda item: item["date"],
                  reverse=True)
    return render(request, 'blog/gui_dang.html', {"data": data})
    # blog_data = Article.objects.all().order_by('-date_time')
    # print(blog_data)
    # return render(request , 'blog/gui_dang.html',{"blog_data" : blog_data})

def Get_Tiezi(request , pk):
    #详细页面
    context = {}
    #通过id获取行的数据
    blog = get_object_or_404(Article, pk=pk)
    blog.viewed()#访问+1
    #格式化md数据
    blog.content = markdown.markdown(blog.content,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])  # 修改blog.content内容为html
    context['blog_content'] = blog
    return render(request, 'blog/blog_detail.html', context)

# def blog_commenced(request,source_id):
#     #添加评论数
#     article = Article.objects.get(pk=source_id)
#     article.commenced()
#     return HttpResponse("提交ok")

def PaiHang(request):
    blog_top = Article.objects.all().order_by('-view')[0:30]
    # blog_top = Article.objects.all().values().order_by('-view')[0:30]
    return render(request , 'blog/pai_hang.html' , {'blog_list' : blog_top ,
                                                    "ab_title" : "排行",
                                                    "ndex_title" : {
                                                        "iso": "el-signal",
                                                        "ins": len(blog_top)
                                                    }
                                                    }

                  )
def LogIn(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        #精准搜素用户名
        result = UserSheet.objects.filter(username=username)
        if result:
            if username == result[0].username and password == result[0].password:
                response = HttpResponse("登录成功")
                ''' max_age 设置过期时间，单位是秒 '''
                # response.set_cookie('name', 'tong', max_age=14 * 24 * 3600)
                ''' expires 设置过期时间，是从现在的时间开始到那个时间结束 '''
                response.set_cookie("e", aes_encrypt(username), expires=datetime.now() + timedelta(days=14))
                response.set_cookie("d", aes_encrypt(password), expires=datetime.now() + timedelta(days=14))
                response.set_cookie("name", username, expires=datetime.now() + timedelta(days=14))

                return response
            else:
                return render(request, 'login/Signin.html', {'errorStr': "账号或密码错误"})
        else:
            return render(request, 'login/Signin.html',{'errorStr' :"账号或密码错误"})

    return render(request, 'login/Signin.html')




def pkcs7padding(text):
    """明文使用PKCS7填充 """
    bs = 16
    length = len(text)
    bytes_length = len(text.encode('utf-8'))
    padding_size = length if (bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    padding_text = chr(padding) * padding
    # coding = chr(padding)
    return text + padding_text

def aes_encrypt(content):
    """ AES加密 """
    cipher = AES.new(b"lfj_cals_lfj_cal", AES.MODE_CBC, b"yNaCoyTzsp83JoQ3")
    # 处理明文
    content_padding = pkcs7padding(content)
    # 加密
    encrypt_bytes = cipher.encrypt(content_padding.encode('utf-8'))
    # 重新编码
    result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
    return result

def aes_decrypt(content):
    """AES解密 """
    cipher = AES.new(b"lfj_cals_lfj_cal", AES.MODE_CBC, b"yNaCoyTzsp83JoQ3")
    content = base64.b64decode(content)
    text = cipher.decrypt(content).decode('utf-8')
    # return text.rstrip(self.coding)
    return text.rstrip("\x0b")



def Register(request):
    #注册
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        mailbox  = request.POST.get("mailbox", None)
        #写入数据
        UserSheet.objects.create(username=username, password=password, mailbox=mailbox)

        response = HttpResponse("注册成功")
        ''' max_age 设置过期时间，单位是秒 '''
        # response.set_cookie('name', 'tong', max_age=14 * 24 * 3600)
        ''' expires 设置过期时间，是从现在的时间开始到那个时间结束 '''
        response.set_cookie("e", aes_encrypt(username), expires=datetime.now() + timedelta(days=14))
        response.set_cookie("d", aes_encrypt(password), expires=datetime.now() + timedelta(days=14))
        response.set_cookie("name", username, expires=datetime.now() + timedelta(days=14))

        return response

    else:
        return render(request, 'login/Register.html')


def GeiBlogTiezo(request):
    #获取博客列表数据
    page_number = get_page(request)
    #数据长度
    blog_count = Article.objects.count()
    #进行算法
    page_info = PageInfo(page_number, blog_count)
    return page_info
