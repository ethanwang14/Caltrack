from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('track/', views.track, name='track'),
    path('history/', views.history, name='history'),
    path('goals/', views.goals, name='goals'),
    path('reset-week/', views.reset_week, name='reset_week'),
]
