from django.core.paginator import Paginator
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from main.models import Challenge, Activity, Challenge_mypage, Stamp, N_badge, Challenge_Badge, CustomUser, Category
import math
from challengeapp.forms import addChallengeForm, PostForm, CategoryForm, StampForm

# Create your views here.
def allchallengeandsearch(request):
    # 페이징 기능 (하단 숫자 리스트)
    all_boards = Challenge.objects.order_by("-challenge_start") # 모든 데이터 조회, 내림차순(-표시) 조회
    paginator = Paginator(all_boards, 5) # 한 페이지당 5개의 글 만 볼 수 있음 => 조절 가능
    page = int(request.GET.get('page', 1))
    board_list = paginator.get_page(page)
    return render(request, 'challengeapp/allchallengeandsearch.html', {'title':'Board List', 'board_list':board_list})

def addchallenge(request, challenge=None):
    if request.method == 'POST':
        form = addChallengeForm(request.POST, request.FILES, instance=challenge)
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.save() 
            return redirect('allchallengeandsearch')
    else:
        form = addChallengeForm
        return render(request, 'challengeapp/addchallenge.html', {'form':form})

def detailchallenge(request, challenge_name):
    challenge = get_object_or_404(Challenge, challenge_name = challenge_name)
    categories = Category.objects
    randomposts = Activity.objects.order_by("?")[:3]
    rankingposts = Activity.objects.order_by("activity_id")[:3]

    return render(request, 'challengeapp/detailchallenge.html', {'challenge' : challenge, 'categories':categories, 'randomposts':randomposts, 'rankingposts':rankingposts})

def challengeedit(request, challenge_name):
    challenge = get_object_or_404(Challenge, challenge_name=challenge_name)
    if request.method == 'POST':
        form = addChallengeForm(request.POST, instance=challenge)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('challengeapp/detailchallenge.html')
    else:
        form = addChallengeForm(instance=challenge)
        return render(request, 'challengeapp/challengeedit.html')

def categoryform(request, category=None):
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            if Category.objects.filter(name=form.cleaned_data['name']):
                form = CategoryForm()
                error_message = "이미 존재하는 카테고리 입니다."
                #카테고리 만드는 팝업창 혹은 페이지로 이동하기
                return render(request, 'challengeapp/challengecategory.html', {'form':form, "error_message":error_message})
            else :
                category.name = form.cleaned_data['name']
                category.save()
            return redirect('allchallengeandsearch')
    else:
        form = CategoryForm(instance=category)
        #카테고리 만드는 팝업창 혹은 페이지로 이동하기
        return render(request, 'challengeapp/challengecategory.html', {'form':form})


def activity(request):
    posts = Activity.objects
    return render(request, 'challengeapp/activity.html', {'posts': posts })

def activitydetail(request, activity_title):
    post = Activity.objects.get(activity_title = activity_title)
    return render(request, 'challengeapp/activitydetail.html', {'post': post})


def mypage(request):
    # 로그인해야지만 들어갈 수 있음
    if not request.user.is_authenticated:
        return HttpResponse("로그인이 필요합니다.")
        
    Custom_user = CustomUser.objects.all()
    stamps = Stamp.objects.all()
    categories = Category.objects # 아직 규빈언니꺼랑 안합쳐서 Category form이 없음.
    posts = Activity.objects
    challenges = Challenge.objects

    return render(request, 'challengeapp/mypage.html', {'Custom_user':Custom_user, 'challegnes':challenges, 'posts': posts, 'categories':categories, 'stamps':stamps})


def newpost(request):
    return render(request, 'challengeapp/newpost.html')

def writepost(request, post=None):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('challengeapp/activity.html')
    else: 
        form = PostForm
        return render(request, 'challengeapp/newpost.html', {'post':post, 'form':form})

def postedit(request, activity_title):
    post = get_object_or_404(Activity, activity_title = activity_title)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('challengeapp/activitydetail.html')
    else:
        form = PostForm(instance=post)
        return render(request, 'challengeapp/postedit.html', {'post':post})


def postdelete(request, activity_title):
    post = get_object_or_404(Activity, activity_title = activity_title)
    post.delete()
    return redirect('activity')

    
def search(request):
    content = Challenge.objects.all() # 모든 object들을 content에 저장
    c = request.GET.get('b','') # GET request의 인자중에 c값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if c:
        content = content.filter(challenge_name__icontains=c)

    return render(request, 'challengeapp/search.html', { 'search':content , 'b':c})

def more(request):
    if 'id' in request.GET:
        challenge = get_object_or_404(Challenge,pk=request.GET.get('id'))
        return render(request, 'challengeapp/more.html', {'post': challenge})
    return HttpResponseRedirect('challengeapp/allchallengeandsearch/')
    

# 선재
# 도장판1
#def mypage(request):
    if request.method == "POST":
        form = StampForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect('main')
    else:
        form = StampForm()
        return render(request, 'challengeapp/mypage.html', {'form':form})

# 도장판2 =  지우꺼랑 합쳐야됨.
#def mypage(request):
    stamps = Stamp.objects.all()
    categories = Category.objects # 아직 규빈언니꺼랑 안합쳐서 Category form이 없음.
    posts = Activity.objects
    challenges = Challenge.objects
    #post = 0
    #if post == 1:
        #challenge_img
    #return render(request, 'challengeapp/mypage.html', {'stamps':stamps}, {'categories':categories}, {'posts': posts})

    #user = request.user # 현재 로그인한 유저
    #stamp.activity_id = 0
    #if stamp.activity_id ==+ 1:

    #stamp.activity_id
   # stamp.challenge_id
    return render(request, 'challengeapp/mypage.html', {'challegnes':challenges, 'posts': posts, 'categories':categories, 'stamps':stamps})
    



# 배지
def badge(request):
    #c_badges = Challenge_Badge.objects.all()
    #categories = Category.objects # 아직 규빈언니꺼랑 안합쳐서 Category form이 없음.
    #posts = Activity.objects
    #challenges = Challenge.objects


    #n_badge = N_badge()
    #c_badge = Challenge_Badge()
    #if request.method == 'POST' :
        #c_badge.challenge_past = 0
        #if c_badge.challenge_past == 30 :
            #n_badge.n30_badge 
        #if c_badge.challenge_past == 50 :
            #n_badge.n50_badge
        #if c_badge.challenge_past == 70 :
            #n_badge.n70_badge
        #if c_badge.challenge_past == 70 :
            #n_badge.n100_badge

        #n_badge.n30_badge
        #n_badge.n50_badge
        #n_badge.n70_badge
        #n_badge.n100_badge
        #n_badge.badge_date 
        #c_badge.challenge_past

    return render(request, 'challengeapp/badge.html')

