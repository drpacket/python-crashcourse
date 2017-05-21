
##################################################
#####'Automate the Boring Stuff with Python' #####
#####		   Book - Exercises				 #####
##################################################

# Divide by Zero Error
##################################################



def spam(divideBy):
	return 42 / divideBy

print(spam(4))

print(spam(15))

print(spam(1))

#	produces Output: "ZeroDivisionError: integer division or modulo by zero"

#print(spam(0))

#	rewrite function to handle Exceptions:

def spam(divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		return("\nInvalid Argument: 0")


print(spam(0))



