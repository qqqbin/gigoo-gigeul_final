from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    nickname = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='images/', blank=True)

class Challenge(models.Model):
    # challenge_id = models.IntegerField()
    challenge_name = models.CharField(max_length = 45)
    #applicant_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applicant_id')
    #participants_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='participants_id')
    categories = models.ManyToManyField('category',blank=True)
    introduction = models.CharField(max_length = 100, null=True)
    challenge_start = models.DateTimeField(auto_now=True)
    #term = models.DateTimeField()
    challenge_img = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.challenge_name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='a_user', primary_key=True)
    challenge_id = models.ForeignKey('main.Challenge', on_delete=models.CASCADE, related_name='myapp.Activity.challenge_id+')
    activity_title = models.CharField(max_length = 45, default="제목을 입력해주세요")
    activity_img = models.ImageField(upload_to='images/', null=True, blank=True)
    activity_content = models.TextField(max_length = 400, null=True)
    activity_date = models.DateTimeField()
    # activity_id = models.IntegerField()

    def __str__(self):
        return self.activity_title

class Challenge_mypage(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='c_user', primary_key=True)
    challenge_ing = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='challenge_ing', null=True)
    challenge_past = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='cmychallenge_past',null=True)

class Stamp(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stp_user', primary_key=True)
    activity_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activity_id', null=True) 
    challenge_id = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='myapp.Stamp.challenge_id+')

    # def __str__(self):
    #     return Challenge.challenge_name

class N_badge(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='nb_user', primary_key=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, max_length = 20, related_name='challenge')
    n30_badge = models.BooleanField(default = True, null=True) 
    n50_badge = models.BooleanField(default = True, null=True) 
    n70_badge = models.BooleanField(default = True, null=True) 
    n100_badge = models.BooleanField(default = True, null=True) 
    badge_date = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, related_name='badge_date')

class Challenge_Badge(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cb_user', primary_key=True)
    challenge_past = models.ForeignKey(Challenge_mypage, on_delete=models.CASCADE, null=True, related_name='cbchallenge_past')

class Shop(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shop_user', primary_key=True)
    addchallenge_id = models.IntegerField(null=True)
    theme_id = models.IntegerField(null=True)
    theme_name = models.CharField(max_length = 45, null=True)
    theme_price = models.IntegerField(null=True)

class Point(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='p_user', primary_key=True)
    user_point = models.IntegerField()
    point_log_name = models.ForeignKey(Shop, on_delete=models.CASCADE, max_length = 45, related_name='point_log_name', null=True)
    point_log_price = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='point_log_price' ,null=True)

class Quiz(models.Model):
    quiz_id = models.IntegerField()
    quiz_content = models.CharField(max_length = 200, null=True)
    quiz_img = models.ImageField(upload_to='images/', null=True, blank=True)
    quiz_true = models.CharField(max_length = 100)
    quiz_false = models.CharField(max_length = 100)
    quiz_explanation = models.CharField(max_length = 300, null=True)
    #quiz_question = models.CharField(max_length = 200)

class Quiz_mypage(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='q_user', primary_key=True)
    quiz_pass = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_pass', null=True)
    quiz_nonepass = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_nonepass', null=True)