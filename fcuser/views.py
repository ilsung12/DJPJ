from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import Fcuser
# Create your views here.

# 이함수를 URL에 연결하면 요청정보가 request라는 변수를 통해서 들어옴.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)

        res_data = {}

        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.' # 예외처리 (POST.get())
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
            #return HttpResponse('비밀번호가 다릅니다.')
        else:
            fcuser = Fcuser(
                username=username,
                password=make_password(password)
            )

            fcuser.save()


        return render(request, 'register.html', res_data)
    
    # templates로 자동을 찾아감.
    # 혹시나 다른 폴더가 있다면 'register.html'<= 이곳에 경로를 적어서 명시해줘야함.
    