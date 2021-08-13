from django.urls import path, include
from userapp import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('editinfo/', views.editinfo, name='editinfo'),
    path('editimage/', views.editimage, name='editimage'),
    path('editpw/', views.editpw, name='editpw'),

    path('findpw/', views.findpw, name='findpw'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signin_page/', views.signin_page, name='signin_page'),
    path('', include('django.contrib.auth.urls')),


    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


    path('account/', include('allauth.urls')),
]