from django.shortcuts import render
from django.views.generic.base import View
from .keyToAdd import KeyToAddress
from decimal import Decimal
import random


class IndexView(View):

    def post(self,request):
        i = int(request.POST.get("page",""))

        data = range(1,0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140)
        # 计算第几页从什么私钥开始取 取多少个
        result = data[200*(int(i)-1):200*(int(i)-1)+200]
        msg = ['没有余额', ]
        list = []
        for key in result:
            values = KeyToAddress(key)
            if values[2] == '可能有余额':
                msg[0]= '此页可能有余额'
            list.append(values)


        page = Decimal(int("0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140",16)//200)
        randomPage = random.randint(1,578960446186580977117854925043439539264187821395374521913025815707590807471)
        content = {'list': list,
                   'page': page,
                   'i': i,
                   'pre_page': i-1,
                   'next_page': i+1,
                   'msg': msg,
                   'randomPage':randomPage
                   }

        return render(request, 'index.html', content)

    def get(self,request):
        i = 1
        data = range(1,0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140)
        #计算第几页从什么私钥开始取 取多少个
        result = data[200*(int(i)-1):200*(int(i)-1)+200]
        msg = ['没有余额',]
        list = []
        for key in result:
            values = KeyToAddress(key)
            if values[2] == '可能有余额':
                msg[0]= '此页可能有余额'
            list.append(values)

        page = Decimal(int("0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140",16)//200)
        randomPage = random.randint(1,578960446186580977117854925043439539264187821395374521913025815707590807471)
        content ={'list':list,
                  'page':page,
                  'i': i,
                  'pre_page':1,
                  'next_page':i+1,
                  'msg':msg,
                  'randomPage':randomPage
                  }

        return render(request,'index.html',content)
