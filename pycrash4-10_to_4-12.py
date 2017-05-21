##################################################
##### 'Python Crash Course' Book - Exercises #####
##################################################

# 4-10. Slices

# take any list/program from this chapter:

# From 4-1. Pizzas: 

pizzas = ["peperoni", "funghi", "calzone", "marinara"]

# Extending list a bit cause its very short
# Using .extend method to add iterable(list) at the end and extend list

pizzas.extend(["diavolo", "quatro stagione", "frutti di mare"])

print(pizzas)

# so now the list 'pizzas' looks like this:
# ['peperoni', 'funghi', 'calzone', 'marinara', 'diavolo', 'quatro stagione', 'frutti di mare']

##################################################

# 4-10. Slices (1)

# print message: "The first three items in the list are: ...

print("\nThe first three items in the list are: "+str(pizzas[0:3]))


# 4-10. Slices (2)

# print same: three items from the middle of the list

print("\nThree items from the middle of the list are:"+str(pizzas[2:5]))


# 4-10. Slices (3)

# print same with last three items: (used negative indexing from back for a change)

print("\nThe last three items in the list are:"+str(pizzas[-3:]))


##################################################

# 4-11. My Pizzas, Your Pizzas

# start with Exercise 4-1.:
# starting with original list of pizzas!

pizzas = ["peperoni", "funghi", "calzone", "marinara"]

# make copy of list. Call friends_pizzas

friends_pizzas = pizzas [:]

# Add new item to each (separate) list

pizzas.append("new york style")

friends_pizzas.append("capricciosa")

# prove that we have two separate lists

# no1 - My Pizzas:

print("\nMy favorite Pizzas are:")
for pizza in pizzas:
	print(pizza)

# no2 - Friends Pizzas:

print("\nMy Friends favorite Pizzas are:")
for pizza in friends_pizzas:
	print(pizza)

##################################################

# 4-12. More Loops:

# ---> get foods.py from Books github page.
# ---> Choose a version of foods.py, write two for-loops to print each list of foods

# foods.py:

my_foods = ['pizza', 'falafel', 'carrot cake'] 

friend_foods = my_foods[:] 

my_foods.append('cannoli') 

friend_foods.append('ice cream') 

# print("My favorite foods are:")
# print(my_foods)
# 
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

print("\nMy favorite foods are:")
for item in my_foods:
	print(item)

print("\nMy friend's favorite foods are:")
for item in friend_foods:
	print(item)


##################################################
##################################################
#---> END



















