"""gigoogigeul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from main import views
from challengeapp import urls
from quizapp import urls
from shopapp import urls
from userapp import urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main, name='main'),
    path('challengeapp/', include('challengeapp.urls')),
    path('quizapp/', include('quizapp.urls')),
    path('shopapp/', include('shopapp.urls')),
    path('userapp/', include('userapp.urls')),
    path('base/', views.main, name='base'),
    # path('signin', views.signin, name='signin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
