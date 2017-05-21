##################################################
##### 'Python Crash Course' Book - Exercises #####
##################################################

# 3-6. More Guests

# Start with program/list from 3-5:

guest_list=['Gerhard', 'Tarek', 'Jussi', 'Bobby', 'Tobi']

for guest in guest_list:
	print 'Hello '+guest+'!', 'I would like to invite you and some other close Friends to Dinner on June 2nd'

# You found a bigger dinner table. Inform guests 

print 'Oh, and by the way - I just managed to find a bigger dinner table, so there will be some more people'

# Think of three more guests to invite 

# Add one new guest to beginning of list with insert() method

guest_list.insert(0,'Flo')

# Add second new guest to the middle of list with insert() method 

guest_list.insert(4,'Julian')

# Add the final third new guest at the end of the list using the append() method

guest_list.append('Felix')


# Print a new set of invitation messages, for every guest in the updated list

for guest in guest_list:
	print 'Hello '+guest+'!', 'I would like to invite you and some other close Friends to Dinner on June 2nd'

# (Print new guest list for reference)

print guest_list


