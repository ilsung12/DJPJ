from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm
    

def home(request):
    return render(request, 'home.html')

def logout(request):
    if request.session.get('user'):
        del (request.session['user'])
        
    return redirect('/')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()


    return render(request, 'login.html', {'form': form})




# 이함수를 URL에 연결하면 요청정보가 request라는 변수를 통해서 들어옴.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.' # 예외처리 (POST.get())
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
            #return HttpResponse('비밀번호가 다릅니다.')
        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )

            fcuser.save()


        return render(request, 'register.html', res_data)
    
    # templates로 자동을 찾아감.
    # 혹시나 다른 폴더가 있다면 'register.html'<= 이곳에 경로를 적어서 명시해줘야함.
    