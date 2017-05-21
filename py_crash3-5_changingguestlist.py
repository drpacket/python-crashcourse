##################################################
##### 'Python Crash Course' Book - Exercises #####
##################################################

# 3-5. Changing Guest List

# You heard that one of the guests in your list from 3-4. can't make it.

# start with program from 3-4.

guest_list=['Gerhard', 'James', 'Jussi', 'Bobby', 'Tobi']

for guest in guest_list:
	print 'Hello '+guest+'!', 'I would like to invite you and some other close Friends to Dinner on June 2nd'

# Add print statement at end of program stating the name of guest
# who can't make it

print 'I am sorry to announce, that '+guest_list[1]+" can't make it"

# Replace person who can't make it with a new guest

del guest_list[1]

guest_list.insert(1,'Tarek')

# Print a second set of invitations for updated list

for guest in guest_list:
	print 'Hello '+guest+'!', 'I would like to invite you and some other close Friends to Dinner on June 2nd'

print guest_list







