from django.urls import path, include
from shopapp import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
]