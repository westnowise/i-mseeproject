from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('<str:key>',views.sort, name='sort'), #키워드 정렬
    path('insert/',views.insert, name='insert'), #전시회 데이터 삽입
     path('<int:pk>/modify/',views.modify, name='modify'), #전시회 데이터 수정
     path('<int:pk>/delete/',views.delete, name='delete'), #전시회 데이터 삭제
    path('mypage/<int:pk>',views.mypage, name='mypage'), #admin mypage
    path('detail/<int:pk>',views.detail, name='detail'),  #전시회 상세 정보 
   
]