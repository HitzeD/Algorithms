#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

	# set variables
	totals = []

	# set a list named `keys` and loops through all the keys in 
	# our recipe and puts them into a list
	keys = list()
	for key in recipe.keys():
		keys.append(key)

	for i in range(len(recipe)):

		count = 0
		
		if ingredients.get(keys[i]) == None or recipe[keys[i]] > ingredients[keys[i]]:
			totals.append(0)

		else:
			
			while (ingredients[keys[i]] - recipe[keys[i]]) >= 0:
				ingredients[keys[i]] = ingredients[keys[i]]  - recipe[keys[i]]
				count += 1 
		totals.append(count)

	return min(totals)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 50, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))