#!/usr/bin/env python
#-*-coding:utf-8-*-

from dao import models

class Tags_handler:
    def __init__(self):
        pass


    def insert_tags(self,name):
        ret = {'status':None,'messages':'','error':''}
        try:
            model = models.Tags.objects.create(name=name)
            print(type(model))
            ret['status']=True
        except Exception as e:
            ret['messages']=e
        return  ret


    def exist_tags(self,name):
        ret = {'status': None, 'messages': '', 'error': ''}
        model=models.Tags.objects.filter('name').first()
        try:
            if model:
                ret['status'] = True
            else:
                models.Tags.objects.create(name=name)
        except Exception as e:
            ret['messages'] = e
        return ret

    def fetch_tags_id(self,name):
        tag_id=[]
<<<<<<< HEAD:dao/Repository/TagRepository.py
        models.UserProfile.objects.filter(name='')
=======
        # models.UserProfile.objects.filter(name='').
>>>>>>> 491462d11e4ad060a0f50c5a7cd04deaf0d75cc7:dao/Repository/TagR.py

    def insert_dao_userprofile_tags(self):
        pass



