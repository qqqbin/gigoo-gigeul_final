from django.shortcuts import render
from main.models import CustomUser, Challenge
import random


# Create your views here.
def main(request):
    Custom_user = CustomUser.objects.all()
    user_count = Custom_user.count()

    challenge = Challenge.objects.all()
    challenge_count = challenge.count()

    # 챌린지를 랜덤으로 나열한 후 3개만
    challenge = Challenge.objects.order_by("?")[:3]

    return render(request, 'main/main.html', {'Custom_user':Custom_user, 'user_count':user_count, 'challenge':challenge, 'challenge_count':challenge_count})

def base(request):
    return render(request, 'main/base.html')