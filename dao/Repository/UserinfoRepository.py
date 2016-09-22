#-*-coding:utf-8-*-
from django.db import models
from dao.migrations.models import *
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse

class fetch_Userinfo:
    def __init__(self):
        pass

    def login(self,request):

        obj = models.UserProfile.objects.filter(username='').first()
        print(obj)
        models.UserProfile.objects.create(caption='')
        aa = models.UserProfile.objects.filter(caption='').all().values('book__name', 'book__page', 'caption')
        print(aa)

        models.Tb1.objects.filter(username='seven').update(gender='0')
        return HttpResponse('添加成功')