from django.shortcuts import render, redirect, get_object_or_404
from .models import ExhibitionDetail
from login.models import Admin_account, Account

#필터 정렬(최신, 키워드))
def sort(request,key):
    login_session = request.session.get('login_session','')
    if login_session == '':  #로그인 X
        login_session= False
        if key=="최신순": #최신순 정렬
            exhibition= ExhibitionDetail.objects.all().order_by('-exhibition_id') #전시회 정보 테이블로부터 생성 id기준 최신 정렬
            filter=False #sort.html에서 드롭다운을 위한 filter 변수
            return render(request, 'Sort/sort.html', {'exhibition':exhibition, 'key':key,'filter':filter,'login_session':login_session})    
        else: #필터정렬
            exhibition=ExhibitionDetail.objects.filter(keyword=key) #키워드 필터링(user가 가지고 있는 key값 기준)
            exhibition=exhibition.order_by('-exhibition_id') #키워드 필터링 후 키워드 s최신순 정렬
            filter=True #sort.html에서 드롭다운을 위한 filter 변수
            return render(request, 'Sort/sort.html', {'exhibition':exhibition, 'key':key,'filter':filter,'login_session':login_session})    
    else: #로그인 O     
        login_session= True
        id=request.session['login_session']  #현재 admin 로그인 세션 정보 받아오기
        user=Account.objects.get(userid=id) #로그인 한 admin 세션으로부터  admin 객체 상세 정보 받아오기
        keyword=user.keyword #admin user의 id값
        if key=="최신순": #최신순 정렬
            exhibition= ExhibitionDetail.objects.all().order_by('-exhibition_id') #전시회 정보 테이블로부터 생성 id기준 최신 정렬
            filter=True #sort.html에서 드롭다운을 위한 filter 변수
            return render(request, 'Sort/sort.html', {'exhibition':exhibition, 'key':key,'keyword':keyword,'filter':filter,'login_session':login_session}) 
        else: #필터정렬
            exhibition=ExhibitionDetail.objects.filter(keyword=key) #키워드 필터링(user가 가지고 있는 key값 기준)
            exhibition=exhibition.order_by('-exhibition_id') #키워드 필터링 후 키워드 s최신순 정렬
            filter=True #sort.html에서 드롭다운을 위한 filter 변수
            return render(request, 'Sort/sort.html', {'exhibition':exhibition, 'key':key,'keyword':keyword,'filter':filter,'login_session':login_session}) 

  

#전시회 데이터 삽입(admin에서만 접근가능)
def insert(request):
    user_id = request.session.get('adminlogin_session') #현재 세션으로부터 admin(관리자) user_id 받아옴
    user = Admin_account.objects.get(userid = user_id) #현재 로그인된 admin세션 기준으로 admin 테이블로부터 user정보 받아오기

    if request.method== "POST":
        exhibition= ExhibitionDetail() #전시회 정보 객체 받아오기
    
        #admin이 입력한 값 POST로 받아오기
        exhibition.title = request.POST['title']
        exhibition.image = request.FILES.get('image')
        exhibition.camera = request.POST['camera']
        exhibition.place=request.POST['place']
        exhibition.info=request.POST['info']
        exhibition.cost=request.POST['cost']
        exhibition.link=request.POST['link']
        exhibition.keyword=request.POST['keyword']
        exhibition.admin=user #admin 객체와 외래키 연결(admin id값->전시 상세정보 글 작성자로 저장(id))
        exhibition.save() #객체에 내용 저장
        # return redirect('sort','최신순')
        return redirect('detail',exhibition.exhibition_id)
    else : # insert.html 띄우기
        return render(request,'insert.html')

#전시회 데이터 수정(admin에서만 접근가능)
def modify(request,pk):
    exhibition_detail= get_object_or_404(ExhibitionDetail,pk=pk) #해당 pk(상세정보 id)값에 맞는 전시회 상세 정보 객체 가져오기
    
    #submit 버튼 누르면 POST요청으로 객체에 정보 저장
    if request.method == "POST":
        exhibition_detail.title = request.POST['title']
        exhibition_detail.image = request.FILES.get('image')
        exhibition_detail.camera = request.POST['camera']
        exhibition_detail.place=request.POST['place']
        exhibition_detail.info=request.POST['info']
        exhibition_detail.cost=request.POST['cost']
        exhibition_detail.link=request.POST['link']
        exhibition_detail.keyword=request.POST['keyword']
            
        exhibition_detail.save()#객체 저장
        return redirect('detail',pk)
    else:
    #내용 수정 전 html 파일에 기존 내용 띄우기 위한 값
        context={ 'title': exhibition_detail.title,
               'image': exhibition_detail.image,
              'camera': exhibition_detail.camera,
              'place':exhibition_detail.place,
              'info':exhibition_detail.info,
              'cost':exhibition_detail.cost,
              'link':exhibition_detail.link,
              'keyword':exhibition_detail.keyword,
              'pk':pk
              }    
        return render(request, 'modify.html', context)

#전시회 데이터 삭제(admin에서만 접근가능)
def delete(reqeust,pk):
    exhibition_detail= get_object_or_404(ExhibitionDetail,pk=pk) #해당 pk값에 맞는 객체 가져오기
    admin=exhibition_detail.admin
    exhibition_detail.delete()
    return redirect('mypage',admin.id)

#admin mypage(자신이 쓴 전시회 데이터 정렬; 삽입, 수정, 삭제 가능)
def mypage(request,pk):
    exhibition=ExhibitionDetail.objects.filter(admin=pk) #admin id(자신의 id)값 기준으로 전시회 정보 정렬
    exhibition=exhibition.order_by('-exhibition_id') #필터링 후 최신순 정렬
    user = Admin_account.objects.get(id = pk) #admin 객체로부터 admin 정보 받아오기; html 화면 구성 위함
    admin=user  #admin값=객체
    return render(request, 'mypage.html', {'exhibition':exhibition, 'admin':admin})    


#전시회 상세 정보
def detail(request,pk):
    exhibition_detail= get_object_or_404(ExhibitionDetail,pk=pk) #전시회 id값에 해당하는 전시회 상세 객체 받아오기
    return render(request,'Detail/detail.html',{'exhibition_detail':exhibition_detail, 'pk':pk})



