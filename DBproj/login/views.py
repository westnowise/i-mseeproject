from django.shortcuts import render, redirect
from .models import Account, Admin_account
from .forms import RegisterForm, LoginForm, AdminRegisterForm,AdminLoginForm
from argon2 import PasswordHasher
# from django.contrib.auth import login as auth_login 

MIN_PASSWORD_LENGTH = 8 

#고침
def index(request):
    context = {}
    login_session = request.session.get('login_session','')
    if login_session == '':
        login_session= False
        context={'login_session':login_session}
        return render(request, 'login/home.html', context)
    else:
        login_session=True
        id=request.session['login_session']
        user=Account.objects.get(userid=id)
        key=user.keyword
        context={'login_session':login_session,
                 'key':key}
        return render(request, 'login/home.html', context)

def signup(request):
    register_form = RegisterForm()
    context = {'forms': register_form}

    if request.method =='GET':
        return render(request,'login/join.html', context)

    elif request.method =='POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = Account(
                userid = register_form.userid,
                password = register_form.password,
                name = register_form.name,
                # keyword = register_form.keyword
            )
            user.save()
            # auth_login(request, user)#회원가입과 동시에 로그인
            login(request)
            # return redirect('/')
            return redirect('test')
            
        else:
            context['forms']=register_form
        return render(request, 'login/join.html', context)


def login(request):
    loginform = LoginForm()
    context = {'forms' : loginform }

    if request.method == 'GET':
        return render(request, 'login/login.html', context)

    elif request.method == 'POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            request.session['login_session'] = loginform.login_session
            request.session['userid'] = loginform.userid
            return redirect('/')
        else:
            context['forms'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request,'login/login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

#admin 회원가입
def adminsignup(request):
    register_form = AdminRegisterForm()
    context = {'forms': register_form}

    if request.method =='GET': #admin 회원가입 폼 렌더링
        return render(request,'login/join.html', context)

    elif request.method =='POST':
        #admin 회원가입 폼에 POST방식으로 회원 정보 담기 
        register_form = AdminRegisterForm(request.POST) 
        if register_form.is_valid():
            user = Admin_account( 
                userid = register_form.userid,
                password = register_form.password,
                name = register_form.name,
                is_staff='True' #관리자 계정 표시
            )
            user.save()#폼 내용 객체에 저장
            adminlogin(request)
            return redirect('adminhome')
        else:
            context['forms']=register_form #잘못된 정보 기입시 다시 회원가입 폼 렌더링
        return render(request, 'login/join.html', context)
    
#admin 로그인   
def adminlogin(request):
    #로그인 폼 받아오기
    loginform = AdminLoginForm() 
    context = {'forms' : loginform }

    if request.method == 'GET': #로그인 폼 렌더링
        return render(request, 'login/adminlogin.html', context)

    #admin 로그인 폼에 POST방식으로 로그인 담기 
    elif request.method == 'POST': 
        loginform = AdminLoginForm(request.POST)
        #로그인 폼에 회원정보가 유효하면 admin 세션열고 저장
        if loginform.is_valid():
            request.session['adminlogin_session'] = loginform.login_session
            return redirect('adminhome')
        else: #로그인 폼에 회원정보가 유효하지 않으면 다시 로그인 폼 렌더링
            context['forms'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request,'login/adminlogin.html', context)
    
    
    
    
#admin 홈(관리자 페이지이므로 주소창으로만 접근 가능)     
def adminhome(request):
    context = {}
    adminlogin_session = request.session.get('adminlogin_session','') #현재 admin 로그인 세션 정보 받아오기
    if adminlogin_session == '':
        adminlogin_session= False #adminhome 화면처리를 위한 장치(로그인 X)
        context={'adminlogin_session':adminlogin_session}
        return render(request, 'login/adminhome.html', context)
    else:
        adminlogin_session=True #adminhome 화면처리를 위한 장치(로그인 O)
        id=request.session['adminlogin_session']  #현재 admin 로그인 세션 정보 받아오기
        user=Admin_account.objects.get(userid=id) #로그인 한 admin 세션으로부터  admin 객체 상세 정보 받아오기
        admin=user.id #admin user의 id값
        context={'adminlogin_session':adminlogin_session,
                 'admin':admin}
        return render(request, 'login/adminhome.html', context)
    
# 테스트
def test(request):
    keyword = request.POST.get('keyword','')

    ## URL 방식이 GET일 경우 POST로 경로 변경
    if request.method =='GET':
        return render(request,'login/test.html')

    ## URL POST일 경우 테스트 진행
    elif request.method =='POST':
        if 'userid' in request.session: # 현재 로그인 상태가 확인되면,
            ## DB에 keword를 추가해 줄 userid를 불러오기 (loginform에서 로그인 시 userid도 저장)
            userid = request.session['userid'] 
            user = Account.objects.get(userid = userid)

            ## account DB table에 저장
            user.keyword = keyword
            user.save()
            key=user.keyword 
            # return redirect('/') #sort 링크로 연결
            # return render(request, 'sort',{key:key})
            return redirect('sort',key)
        else: # 현재 로그인 상태가 아니면 로그인 화면 출력
            # return render(request, 'login/login.html') #원래 이게 맞는거임
            return redirect('/')
