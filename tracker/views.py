from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Sum
from .models import UserProfile, Goals, FoodEntry
from .forms import FoodEntryForm, GoalsForm
import math

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile and default goals
            UserProfile.objects.create(user=user)
            Goals.objects.create(user=user)
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'tracker/login.html')

@login_required
def home(request):
    # Get user's goals
    goals, created = Goals.objects.get_or_create(user=request.user)
    
    # Calculate weekly totals
    weekly_totals = FoodEntry.objects.filter(user=request.user).aggregate(
        total_calories=Sum('calories'),
        total_protein=Sum('protein'),
        total_carbs=Sum('carbs'),
        total_fats=Sum('fats')
    )
    
    # Convert None to 0 for display
    totals = {
        'calories': weekly_totals['total_calories'] or 0,
        'protein': weekly_totals['total_protein'] or 0,
        'carbs': weekly_totals['total_carbs'] or 0,
        'fats': weekly_totals['total_fats'] or 0,
    }
    
    # Calculate progress percentages
    progress = {}
    for nutrient in ['calories', 'protein', 'carbs', 'fats']:
        goal = getattr(goals, f'{nutrient}_goal')
        current = totals[nutrient]
        if goal > 0:
            progress[nutrient] = min(100, (current / goal) * 100)
        else:
            progress[nutrient] = 0
    
    context = {
        'totals': totals,
        'goals': goals,
        'progress': progress,
    }
    return render(request, 'tracker/home.html', context)

@login_required
def track(request):
    if request.method == 'POST':
        form = FoodEntryForm(request.POST)
        if form.is_valid():
            food_entry = form.save(commit=False)
            food_entry.user = request.user
            food_entry.save()
            messages.success(request, f'Added {food_entry.name} to your nutrition log!')
            return redirect('track')
    else:
        form = FoodEntryForm()
    
    return render(request, 'tracker/track.html', {'form': form})

@login_required
def history(request):
    entries = FoodEntry.objects.filter(user=request.user)
    return render(request, 'tracker/history.html', {'entries': entries})

@login_required
def goals(request):
    goals, created = Goals.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = GoalsForm(request.POST, instance=goals)
        if form.is_valid():
            form.save()
            messages.success(request, 'Goals updated successfully!')
            return redirect('goals')
    else:
        form = GoalsForm(instance=goals)
    
    return render(request, 'tracker/goals.html', {'form': form})

@login_required
def reset_week(request):
    if request.method == 'POST':
        FoodEntry.objects.filter(user=request.user).delete()
        messages.success(request, 'Week reset successfully! All entries have been cleared.')
        return redirect('home')
    
    return render(request, 'tracker/reset_week.html')
