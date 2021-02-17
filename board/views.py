from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# 일단 Loader import, Loader은 templete를 loading 시켜주는 역할을 한다.
from datetime import datetime
# datetime 모듈을 가져온다.


# def index(ref):
#     return HttpResponse("아잇")



def select(req, value):
    message = '숫자를 입력해주세요' + str(value)
    return HttpResponse(message)

    
def result(req):
    message = '추첨 결과 입니다.'
    return HttpResponse(message)

def index(req):
    template = loader.get_template('index.html')
# template 변수에 loader.get_template(가져올 곳 - templates 폴더에 있어야한다.) 을 주어 template를 가져옴

    now = datetime.now() # 현재시간 할당
    print((now))
    context = {  
        'currenet_date' : now
        #value' : 2,
    }
        # context object 파일에 now를 추가한다. 
        # 참고로 context는 서버에서 해당페이지에 데이터를 넘겨줄 때 사용 한다. 
        # value도 하나 준다.
    return HttpResponse(template.render(context, req))
        # 그리고 HttpResponse에 template.render(context.req)를 준다.
        # template.render로 context를 주고, req를 주어 데이터를 전송하는 것 이다.

