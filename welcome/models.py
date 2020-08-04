from django.db import models

# Create your models here.


class UserInfo(models.Model):
    date = models.DateField()   #日期
    userName = models.CharField(max_length=32) #员工名
    teamLeader = models.CharField(max_length=32) #tl
    callCount = models.IntegerField()   #外呼次数
    callsucessCount = models.IntegerField() #接通次数
    callTime = models.IntegerField()    #通时
    touchNum = models.IntegerField()    #触达数
    touchCompanyNum = models.IntegerField() #触达企业数
    communicationNum = models.IntegerField()    #沟通数
    communicationCompanyNum = models.IntegerField() #沟通企业数
    intentionCount = models.IntegerField()  #意向客户数
    order = models.IntegerField()   #订单数
    cash = models.IntegerField()    #订单金额
