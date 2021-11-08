from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    nickname = models.CharField(max_length=20) #기본사용자닉네임
    profile_image = models.ImageField(upload_to='images/', blank=True) #프로필이미지

class Challenge(models.Model): #챌린지
    # challenge_id = models.IntegerField() #챌린지ID
    challenge_name = models.CharField(max_length = 45) #챌린지이름
    #applicant_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applicant_id') #챌린지신청자ID
    #participants_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='participants_id') #챌린지참가자ID
    categories = models.ManyToManyField('category',blank=True)  #챌린지카테고리
    introduction = models.CharField(max_length = 100, null=True)    #챌린지소개
    challenge_start = models.DateTimeField(auto_now=True)   #챌린지 시작일
    #term = models.DateTimeField()  #챌린지실행기간 
    challenge_img = models.ImageField(upload_to='images/', blank=True) #챌린지대표이미지

    def __str__(self):
        return self.challenge_name

class Category(models.Model): #챌린지카테고리
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Activity(models.Model): #챌린지내의활동
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='a_user', primary_key=True) #작성자ID
    challenge_id = models.ForeignKey('main.Challenge', on_delete=models.CASCADE, related_name='myapp.Activity.challenge_id+') #챌린지ID
    activity_title = models.CharField(max_length = 45, default="제목을 입력해주세요") #활동제목
    activity_img = models.ImageField(upload_to='images/', null=True, blank=True) #활동사진
    activity_content = models.TextField(max_length = 400, null=True) #활동내용
    activity_date = models.DateTimeField() #활동날짜
    # activity_id = models.IntegerField() #활동ID

    def __str__(self):
        return self.activity_title

class Challenge_mypage(models.Model): #마이페이지 
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='c_user', primary_key=True) #해당사용자ID
    challenge_ing = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='challenge_ing', null=True) #현재진행중인챌린지
    challenge_past = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='cmychallenge_past',null=True) #완료한챌린지

class Stamp(models.Model): #도장
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stp_user', primary_key=True) #해당사용자ID
    activity_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activity_id', null=True) #활동ID
    challenge_id = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='myapp.Stamp.challenge_id+') #챌린지ID

    # def __str__(self):
    #     return Challenge.challenge_name

class N_badge(models.Model): #뱃지
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='nb_user', primary_key=True) #해당사용자ID
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, max_length = 20, related_name='challenge') #챌린지이름
    n30_badge = models.BooleanField(default = True, null=True) #활동횟수가30회될때지급되는뱃지
    n50_badge = models.BooleanField(default = True, null=True) #활동횟수가50회될때지급되는뱃지
    n70_badge = models.BooleanField(default = True, null=True) #활동횟수가70회될때지급되는뱃지
    n100_badge = models.BooleanField(default = True, null=True) #활동횟수가100회될때지급되는뱃지
    badge_date = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, related_name='badge_date') #뱃지적립날짜

class Challenge_Badge(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cb_user', primary_key=True) #해당사용자ID
    challenge_past = models.ForeignKey(Challenge_mypage, on_delete=models.CASCADE, null=True, related_name='cbchallenge_past') #완료한챌린지

class Shop(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shop_user', primary_key=True) #해당사용자ID
    addchallenge_id = models.IntegerField(null=True) #추가하는챌린지ID
    theme_id = models.IntegerField(null=True) #테마ID
    theme_name = models.CharField(max_length = 45, null=True) #테마이름
    theme_price = models.IntegerField(null=True) #테마가격

class Point(models.Model): #포인트
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='p_user', primary_key=True) #해당사용자ID
    user_point = models.IntegerField() #포인트
    point_log_name = models.ForeignKey(Shop, on_delete=models.CASCADE, max_length = 45, related_name='point_log_name', null=True) #포인트사용내역(항목이름)
    point_log_price = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='point_log_price' ,null=True) #포인트사용내역(가격)

class Quiz(models.Model): #퀴즈
    quiz_id = models.IntegerField() #퀴즈별ID
    quiz_content = models.CharField(max_length = 200, null=True) #퀴즈내용
    quiz_img = models.ImageField(upload_to='images/', null=True, blank=True) #퀴즈이미지
    quiz_true = models.CharField(max_length = 100) #퀴즈정답
    quiz_false = models.CharField(max_length = 100) #퀴즈오답
    quiz_explanation = models.CharField(max_length = 300, null=True) #퀴즈해설
    #quiz_question = models.CharField(max_length = 200) #퀴즈문제

class Quiz_mypage(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='q_user', primary_key=True) #해당사용자ID
    quiz_pass = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_pass', null=True) #맞힌퀴즈
    quiz_nonepass = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_nonepass', null=True) #
