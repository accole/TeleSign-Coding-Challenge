from django import forms

class addForm(forms.Form):
	Item_Name = forms.CharField()
	Snack_or_Drink = forms.CharField()
	Number_of_Ingredients = forms.IntegerField()

class deleteForm(forms.Form):
	Snack_or_Drink = forms.CharField()
	Item_Name = forms.CharField()

class ingredForm(forms.Form):
	Ingredient = forms.CharField()