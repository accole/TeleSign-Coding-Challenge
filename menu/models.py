from django.db import models

# Create your models here.

#######################################################################3


# Menu items have a name, and a toString() method
class MenuItem(models.Model):
	item = models.CharField(max_length=10)
	def __str__(self):
		return self.item

# Drinks are menu items, and have reccommended snack pairs
class Drink(MenuItem):
	drink_name = models.CharField(max_length=75)
	#reccomend = models.ManyToManyField('Snack')
	def __str__(self):
		return self.drink_name

# Snacks are menu items, and have reccommended drink pairs
class Snack(MenuItem):
	snack_name = models.CharField(max_length=75)
	reccomend = models.ManyToManyField(Drink)
	def __str__(self):
		return self.snack_name


#########################################################################


# multiple Ingredients can be in any Menu Item
class Ingredient(models.Model):
	ingred_name = models.CharField(max_length=75)
	ingredients = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
	def __str__(self):
		return self.ingred_name