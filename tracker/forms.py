from django import forms
from .models import FoodEntry, Goals

class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ['name', 'calories', 'protein', 'carbs', 'fats']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name of food/drink'}),
            'calories': forms.NumberInput(attrs={'placeholder': 'Calories'}),
            'protein': forms.NumberInput(attrs={'placeholder': 'Protein (g)'}),
            'carbs': forms.NumberInput(attrs={'placeholder': 'Carbs (g)'}),
            'fats': forms.NumberInput(attrs={'placeholder': 'Fats (g)'}),
        }
    
    def clean_calories(self):
        calories = self.cleaned_data.get('calories')
        if calories is not None:
            return int(calories)
        return calories
    
    def clean_protein(self):
        protein = self.cleaned_data.get('protein')
        if protein is not None:
            return int(protein)
        return protein
    
    def clean_carbs(self):
        carbs = self.cleaned_data.get('carbs')
        if carbs is not None:
            return int(carbs)
        return carbs
    
    def clean_fats(self):
        fats = self.cleaned_data.get('fats')
        if fats is not None:
            return int(fats)
        return fats

class GoalsForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = ['calories_goal', 'protein_goal', 'carbs_goal', 'fats_goal']
        widgets = {
            'calories_goal': forms.NumberInput(attrs={'placeholder': 'Weekly calories goal'}),
            'protein_goal': forms.NumberInput(attrs={'placeholder': 'Weekly protein goal (g)'}),
            'carbs_goal': forms.NumberInput(attrs={'placeholder': 'Weekly carbs goal (g)'}),
            'fats_goal': forms.NumberInput(attrs={'placeholder': 'Weekly fats goal (g)'}),
        }
    
    def clean_calories_goal(self):
        calories_goal = self.cleaned_data.get('calories_goal')
        if calories_goal is not None:
            return int(calories_goal)
        return calories_goal
    
    def clean_protein_goal(self):
        protein_goal = self.cleaned_data.get('protein_goal')
        if protein_goal is not None:
            return int(protein_goal)
        return protein_goal
    
    def clean_carbs_goal(self):
        carbs_goal = self.cleaned_data.get('carbs_goal')
        if carbs_goal is not None:
            return int(carbs_goal)
        return carbs_goal
    
    def clean_fats_goal(self):
        fats_goal = self.cleaned_data.get('fats_goal')
        if fats_goal is not None:
            return int(fats_goal)
        return fats_goal
