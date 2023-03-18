from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'), #일반 회원가입
    path('login', views.login, name='login'), #일반 회원 로그인
    path('adminsignup', views.adminsignup, name='adminsignup'), #admin 회원가입
    path('adminlogin', views.adminlogin, name='adminlogin'), #admin 로그인
    path('logout', views.logout, name='logout'), #일반 회원 및 admin 로그아웃
    path('test', views.test, name = 'test'), # 테스트로 이동하는 url
]
