from django import forms
from main.models import Category, Challenge, Activity, Stamp, N_badge, Challenge_Badge


class addChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['challenge_name', 'introduction', 'categories', 'challenge_img']
        labels = {'challenge_name': '챌린지 이름', 'introduction': '챌린지 소개', 'categories': '카테고리', 'challenge_img': '챌린지 사진'}

class PostForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['challenge_id','activity_title', 'activity_date', 'activity_img', 'activity_content']
        labels = {'challenge_id': "챌린지 종류",'activity_title': '활용 내역', 'activity_date': '활동 날짜', 'activity_img': '활동 사진', 'activity_content': '활동 내용'}


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name'] 
        labels ={'name':"카테고리 이름"}

# 선재
class StampForm(forms.ModelForm):
    class Meta:
        model = Stamp
        fields = ['id', 'challenge_id', 'challenge_id']

# 선재
class N_BadgeForm(forms.ModelForm):
    class Meta:
        model = N_badge
        fields = ['id', 'challenge', 'n30_badge', 'n50_badge', 'n70_badge', 'n100_badge', 'badge_date']

# 선재
class Challenge_BadgeForm(forms.ModelForm):
    class Meta:
        model = Challenge_Badge
        fields = ['id', 'challenge_past']