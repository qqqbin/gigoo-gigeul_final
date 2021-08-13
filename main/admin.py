from django.contrib import admin
from .models import Activity, Challenge, Challenge_Badge, Challenge_mypage, CustomUser, N_badge, Point, Quiz, Quiz_mypage, Shop, Stamp

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Challenge)
admin.site.register(Activity)
admin.site.register(Challenge_mypage)
admin.site.register(Stamp)
admin.site.register(N_badge)
admin.site.register(Challenge_Badge)
admin.site.register(Shop)
admin.site.register(Point)
admin.site.register(Quiz)
admin.site.register(Quiz_mypage)