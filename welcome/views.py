import json

from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
# from django.shortcuts import render_to_response


# 接收POST请求数据
from welcome.forms import UploadFileForm


def index(request):
    dicOrder, dicCash, dicCC, dicCT, dicATT = {}, {}, {}, {}, {}
    #lstTL = ['陈文清', '宋成鑫', '冉青青', '罗舒', '汪吴水', '尚玮', '侯妞妞']
    lstTL = ['转化', '留存']

    # for i in lstTL:
    #     if i is '陈文清' or i is '宋成鑫':
    #         dicOrder[i] = {'stack': '转化组', 'data': [2, 4, 6, 8, 10]}
    #     else:
    #         dicOrder[i] = {'stack': '留存组', 'data': [2, 4, 6, 8, 10]}

    for i in lstTL:
        if i is '转化':
            dicOrder[i] = {'stack': '转化组', 'data': [2, 4, 6, 8, 10]}
        else:
            dicOrder[i] = {'stack': '留存组', 'data': [1, 3, 5, 7, 9]}

    dicParam = {'lstTLname': json.dumps(lstTL), 'order_series': dicOrder, 'cash_series': dicCash, 'callcount_series': dicCC,
                'calltime_series': dicCT, 'ATT_series': dicATT}


    return render(request, "index.html", dicParam)


def team(request):
    lstmember = ['1', "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    lstData = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    lstPercentage = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
    dicParam = {'data': lstData, 'percentage': lstPercentage, 'member': json.dumps(lstmember)}
    return render(request, "team.html", dicParam)


def personal(request):
    lstmember = ['1', "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    lstData = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    lstPercentage = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
    usr = '某员工'
    teamname = '转化组'
    lstPersonal = [20, 30, 90, 50, 50]
    lstAvg = [40, 40, 40, 40, 40]
    dicParam = {'data': lstData, 'percentage': lstPercentage, 'member': json.dumps(lstmember), 'name': usr,
                'teamname': teamname, 'personal': lstPersonal, 'avg':lstAvg}
    return render(request, "personal.html",  dicParam)


def uploadfilepage(request):
    upform = UploadFileForm()
    return render(request, 'upload_file.html', {'form': upform})


def upload_file(request):
    if request.method == 'POST':
        upform = UploadFileForm(request.POST, request.FILES)
        if upform.is_valid():
            f = upform.cleaned_data['upfile']
            if handle_uploaded_file(f):
                return HttpResponse('上传成功')
            else:
                upform = UploadFileForm()
                return render(request, 'upload_file.html', {'form': upform, 'tip': "错误！ 样例:通时文件xx.xlsx 或者 成单排行榜.xlsx"})
    upform = UploadFileForm()
    return render(request, 'upload_file.html', {'form': upform})


def handle_uploaded_file(f):
    print(f.name, f.name.find('成单排行榜'))
    if f.name.find('通时') < 0 and f.name.find('成单排行榜') < 0:
        return False

    with open("./welcome/upfile/"+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

        return True

    return False

