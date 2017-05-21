##################################################
##### 'Python Crash Course' Book - Exercises #####
##################################################

# 4-3. Counting to Twenty

for i in range(1,21):
	print(i)

##################################################

# 4-4. One Million ( using 'List Comprehension' ) 
# >> COMMENTED OUT CAUSE OF LONG RUN TIME !!!(Ctrl-C no work):

# print([number for number in range(1,1000001)])

##################################################

# 4-5. Summing a Million, min(), max(), sum()

million_list = list(range(1, 1000001))

# print(million_list)

print(min(million_list))

print(max(million_list))

print(sum(million_list))

##################################################

# 4-6. Odd Numbers

# (list comprehension with conditional - testing)

odds = [number for number in range(1,21) if number % 2 != 0]
print(odds)

# regular

odd_numbers = list(range(1,21,2))

for odd in odd_numbers:
	print(odd)

##################################################

# 4-7.Threes

# multiples of 3 from 3 to 30

for value in range(3, 31, 3):
	print(value)

##################################################

# 4-8. Cubes

# list of first 10 cubes(n**3) of each int from 1 through 10

# (using List Comprehension)
cubes_list = [n**3 for n in range(1,11)]

print(cubes_list,"\n")

for cube in cubes_list:
	print(cube)

# regular

for i in range(1, 11):
	print(i**3)

##################################################

# 4-9. Cube Comprehension

# -->> see line 63 of 4-8. Cubes.
# Again:

cube_list = [i**3 for i in range(1, 11)]

print(cube_list)














