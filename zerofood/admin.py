from django.contrib import admin

from .models import UserType, FoodType, FoodState, Profile

admin.site.register(UserType)
admin.site.register(FoodType)
admin.site.register(FoodState)
admin.site.register(Profile)
