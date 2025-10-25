from django.contrib import admin
from .models import UserProfile, Goals, FoodEntry

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user__email']
    search_fields = ['user__username', 'user__email']

@admin.register(Goals)
class GoalsAdmin(admin.ModelAdmin):
    list_display = ['user', 'calories_goal', 'protein_goal', 'carbs_goal', 'fats_goal']
    search_fields = ['user__username']

@admin.register(FoodEntry)
class FoodEntryAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'calories', 'protein', 'carbs', 'fats', 'date_added']
    list_filter = ['date_added', 'user']
    search_fields = ['name', 'user__username']
    ordering = ['-date_added']
