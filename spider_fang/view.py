from django.shortcuts import render
from house.models import *
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.http import HttpResponse
from pymysql import connect,cursors
my=connect('localhost','root','wy236512','pachong')
from django.db.models import Min,Avg,Max,Sum,Count
#zyh815115  密码   loupan 数据库名
cu = my.cursor(cursors.DictCursor)
# def home(request):
#     if request.method=='GET':
#         home_type=[]
#         homes=Home.objects.filter(home_type__isnull=False)
#         for i in homes:
#             home_type.append(i.home_type)
#         info_id=[]
#         city_id=City.objects.filter(city__isnull=False)
#         for i in city_id:
#             info = Info.objects.filter(cid=i)
#
#             info_id.append({'li':info,'cid':i})
#
#
#         print(info_id)
#         return render(request, '../templates/tongjitu.html', {'homes':homes})
# def new(request):
#     if request.method == 'GET':
#         info_id = []
#         city_id = City.objects.filter(city__isnull=False)
#         for i in city_id:
#             print(i)
#             info = Info.objects.filter(cid=i)
#
#             info_id.append({'li': info, 'cid': i})
#
#         return render(request, '../templates/new.html', {'info_id':info_id,})

def city(request):
    if request.method == 'GET':
        list1 = []
        home=[]
        citys = City.objects.filter(city__isnull=False)
        for i in citys:
            a=Info.objects.filter(cid=i.id).count()
            home.append(a)

        print('aaaaaaaaaaaaaaaaaa',home)
        for i in citys:

            list1.append(i.city)

        return render(request, '../templates/city.html', {'citys':list1,'home':home})


def tj(request):
    if request.method=='GET':
        pp=[]
        aa=[]
        homes=Home.objects.filter(home_type__isnull=False)
        for i in homes:
            aa.append(i.home_type)
            a = Info.objects.filter(hid=i.id).count()
            pp.append({'value':a,'name':i.home_type})
        return render(request, '../templates/tongjitu.html', {'pp':pp,'aa':aa})

