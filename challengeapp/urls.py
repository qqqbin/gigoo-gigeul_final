from django.urls import path, include
from challengeapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('allchallengeandsearch/', views.allchallengeandsearch, name='allchallengeandsearch'),
    path('addchallenge/', views.addchallenge, name='addchallenge'),
    path('detailchallenge/', views.detailchallenge, name='detailchallenge'),
    path('challengecategory/',views.categoryform, name='challengecategory'),
    path('challengeedit/', views.challengeedit, name='challengeedit'),
    path('activity/', views.activity, name='activity'),
    path('activitydetail/<str:activity_title>/', views.activitydetail, name='activitydetail'),
    path('mypage/', views.mypage, name='mypage'),
    path('newpost/writepost/', views.writepost, name='writepost'),
    path('postedit/<str:activity_title>/', views.postedit, name='postedit'),
    path('postdelete/<str:activity_title>/', views.postdelete, name='postdelete'),
    path('badge/', views.badge, name='badge'),
    path('search/', views.search, name='search'),
    path('more', views.more, name='more'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)