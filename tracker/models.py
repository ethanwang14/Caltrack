from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class Goals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    calories_goal = models.IntegerField(default=0)
    protein_goal = models.IntegerField(default=0)
    carbs_goal = models.IntegerField(default=0)
    fats_goal = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Goals"
    
    def __str__(self):
        return f"{self.user.username}'s Goals"

class FoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    calories = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    fats = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Food Entries"
        ordering = ['-date_added']
    
    def __str__(self):
        return f"{self.name} - {self.user.username}"
