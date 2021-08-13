from django.urls import path, include
from quizapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('detailquiz/', views.detailquiz, name='detailquiz'),
    path('detailquiznote/', views.detailquiznote, name='detailquiznote'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiznote/', views.quiznote, name='quiznote'),
]