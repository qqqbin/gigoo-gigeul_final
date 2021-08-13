from django.core.paginator import Paginator
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from main.models import Quiz, Quiz_mypage, CustomUser
from quizapp.forms import QuizForm
from main.models import CustomUser

# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# Create your views here.

# 오답노트에 있는 내가 푼 퀴즈들의 상세 설명을 보는 곳
def detailquiz(request): 
    return render(request, 'quizapp/detailquiz.html')

"""
def detailquiz(request): 
    p_or = get_object_or_404(Quiz_mypage)
    return render(request, 'quizapp/detailquiz.html', {'p_or': p_or})
"""

# 퀴즈 설명보는 곳
def detailquiznote(request): 
    return render(request, 'quizapp/detailquiznote.html')

"""
def detailquiznote(request): 
    quiz_form = QuizForm()
    quiz = get_object_or_404(Quiz)
    quizs = Quiz.objects


    return render(request, 'quizapp/detailquiznote.html', {'quiz':quiz})
"""

# 퀴즈푸는 곳
def quiz(request):
    return render(request, 'quizapp/quiz.html')

"""""
def quiz(request):
    quiz_form = QuizForm()
    quiz = get_object_or_404(Quiz)
    quizs = Quiz.objects


 
    if request.method == 'GET':
        # 정답고르기 'O' 골랐을때
        if request.GET.get('O'):
            return redirect('detailquiznote')
        
        return render(request, 'quizapp/quiz.html', {'quizs':quizs})

    elif request.method == 'POST':
        # 정답고르기 'X' 골랐을때
        if request.GET.get('X'):
            return redirect('detailquiznote')

        return render(request, 'quizapp/quiz.html', {'quizs':quizs})
"""
        
    #if request.method == 'POST':
        #form = QuizForm(request.POST)
        #if form is valid():
            #quiz = form.save(commit=False)
            #quiz.quiz_id 
            #quiz.quiz_img
            #quiz.quiz_content
            #quiz.quiz_true
            #quiz.quiz_false
            #quiz.quiz_explanation
            #quiz.quiz_question
            #quiz.save()

    #return render(request, 'quizapp/quiz.html', {'quiz':quiz})


# 내가 푼 퀴즈들 오답노트 (한 눈에 볼 수 있는 페이지)
def quiznote(request):
    #por_list = Quiz_mypage.objects.all()
    return render(request, 'quizapp/quiznote.html', #{'por_list':por_list}
    )


