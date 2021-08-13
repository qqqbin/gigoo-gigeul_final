from django.shortcuts import get_object_or_404, redirect, render
from .forms import SigninForm, UserForm
from main.models import CustomUser
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from django.views.generic.detail import DetailView
from django.views import View

# 비밀번호 재설정 import
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.urls import reverse_lazy



# Create your views here.
@login_required
def editinfo(request):
    if request.method == 'GET':
        return render(request, 'userapp/editinfo.html')

    elif request.method == 'POST':
        user = request.user
        email = request.POST.get('email')
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')

        user.email = email
        user.username = username
        user.nickname = nickname

        user.save()

        return redirect('mypage')


@login_required
def editimage(request):
    Custom_user = CustomUser.objects.all()
    user = request.user

    if request.method == 'GET':
        # 프로필 삭제
        if request.GET.get('d'):
            user.profile_image.delete()
            return redirect('mypage')
            
        return render(request, 'userapp/editimage.html', {'Custom_user':Custom_user})

    elif request.method == 'POST':
        # 아무 사진 선택하지 않고 제출 => 프사 유지
        if not request.FILES:
            user.profile_image
        # 다른 프로필 사진으로 변경
        else:
            profile_image = request.FILES['profile_image']
            user.profile_image = profile_image

        user.save()

        return redirect('mypage')


@login_required
def editpw(request):
    Custom_user = CustomUser.objects.all()

    if request.method == 'GET':
        return render(request, 'userapp/editpw.html', {'Custom_user':Custom_user})

    elif request.method == 'POST':
        user = request.user
        pw = request.POST.get('pw')

        user.set_password(pw)
        user.save()

        return redirect('main')



def findpw(request):
    return render(request, 'userapp/findpw.html')

def signin_page(request):
    signin_form = SigninForm()
    return render(request, 'userapp/signin_page.html', {'signin_form': signin_form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = CustomUser.objects.create_user(username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            nickname=form.cleaned_data['nickname'],
            profile_image=form.cleaned_data['profile_image'])
            login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('main')
        # else:
        #     return HttpResponse('실패')
    else:
        form = UserForm()
        return render(request, 'userapp/signup.html', {'form': form})

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return HttpResponse("로그인 실패")

# 비밀번호 재설정
class MyPasswordResetView(PasswordResetView):
    success_url=reverse_lazy('login')
    template_name = 'userapp/password_reset_form.html'
    email_template_name = 'userapp/password_reset.html'
    mail_title="비밀번호 재설정"

    def form_valid(self, form):
        return super().form_valid(form)

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    success_url=reverse_lazy('login')
    template_name = 'userapp/password_reset_confirm.html'

    def form_valid(self, form):
        return super().form_valid(form)
