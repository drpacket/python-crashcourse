##################################################
##### 'Python Crash Course' Book - Exercises #####
##################################################
# 5-1. Conditional Tests:
# create a Number of conditional tests (10 suggested if no Exp. - I'll do 5;)

#1
audi = "Blue Flag" 

n = 5
while audi == "Blue Flag" and n >= 0:
	print("Blue")
	n -= 1

#Condition True, will print "Blue" 6 times then end
s = "ahgaagsddagsdaaagdfaaaa"

##################################################
#2
count = 0
for char in s:
	if char == "a":
		count += 1
print("\nCharacter 'a' was included "+str(count)+" times in string s\n")

# will count no of a's and then after for-loop is finished prints out sentence below
# including the no of a's in string s

##################################################

#3
dogs = "sdfkjldoglksjdlkjsdfdoglkjsdkljdoglklkjlkdsfdog"

iter = 0
dogcount = ""

while len(dogcount) <= 3:
	for char in dogs.lower():
		dogcount += char
		iter += 1
		if dogcount == "dog":
			print("Bark!\n")
		print(iter)
print("Grrrrrrrr... * Music playing * 'This is the End ... my only Friend the End...'")


# PAUSED  --- ALSO WILL ONLY DO 5 EXAMPLES - NOT 10. got enough basic conditinals
# and getting to much into stupid timeconsuming stuff here instead of moving on...

##################################################

#4
x = 45
print("\nEnter a 2-digit Number please! If u have guessed it right, u win!")
while True:
	guess = input(">")
	if int(guess) == 45:
		break
print("Congrats! U have guessed the right Number! It was: "+str(guess))

##################################################

#5
sandwich = input("Pick your choice of Sandwich:> ").lower()

sub_of_day = "Tuna and Lettuce"

if sandwich == sub_of_day:
	print("Congratulations! Enjoy our custom-made Sub of the Day.")
else:
	print("Pick an item on the Menu please")

##################################################

sandwiches = ["Tuna and Lettuce", "Ham", "Cheese", "Macaroni", "Bologni"]

print(sandwiches)

while True:
	pick = input("Pick a Sandwich from our Menu. Press EXIT to exit: ")
	
	if pick in sandwiches:
		print("Your Item will be ready shortly!")
	elif pick == "exit".upper():
		break
	else:
		print("You need to pick something from our menu.")


##################################################
#---> ENDE


