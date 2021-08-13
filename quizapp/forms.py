from django import forms
from main.models import Quiz, Quiz_mypage
# from django.contrib.auth.models import User

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['quiz_id', 'quiz_content', 'quiz_img', 'quiz_true', 'quiz_false', 'quiz_explanation']

#class Quiz_mypageForm(forms.ModelForm):
    #class Meta:
        #model = Quiz_mypage
        #fields = ['quiz_p', 'quiz_np']