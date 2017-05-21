##################################################
##### 'Python Crash Course' Book - Exercises #####
##################################################

# 3-2. Greetings

# Start with List 'friends' from 3-1. and print a personalized
# Greeting to every friend in the list...


friends=['Felix', 'Mathias', 'Marco', 'Feri', 'Julian']

#simple version with slicing of list, repeated:

print'Hello',friends[0]+'!','I hope u had a really nice day!'
print'Hello',friends[1]+'!','I hope u had a really nice day!'
print'Hello',friends[2]+'!','I hope u had a really nice day!'
print'Hello',friends[3]+'!','I hope u had a really nice day!'
print'Hello',friends[4]+'!','I hope u had a really nice day!'

# Version with for loop:

for friend in friends:
	print 'Hey there,', friend+'!', 'I hope u had a really nice day!'

