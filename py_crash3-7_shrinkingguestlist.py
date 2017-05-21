##################################################
##### 'Python Crash Course' Book - Exercises #####
##################################################

# 3-7. Shrinking Guest List

# Start with program/list from Exercise 3-6.

guest_list=['Flo', 'Gerhard', 'Tarek', 'Jussi', 'Julian', 'Bobby', 'Tobi', 'Felix']

print guest_list

# You suddenly have room for only two guests, because your new table won't
# arrive in time for the dinner

# Add new line: message saying that (now) you can invite only two people 

print "So sorry guys! My new table won't arrive in time. Looks like I can invite only two people for dinner after all..."

# Use pop() to remove guests from list until only two remain
# After every pop() let the person 'popped' know that you're sorry you can't invite him/her
# ... until there are only TWO people left...

popped_guest=guest_list.pop()

print 'Sorry '+popped_guest+' - I could not invite you after all!'

popped_guest=guest_list.pop()

print 'Sorry '+popped_guest+' - I could not invite you after all!'

popped_guest=guest_list.pop()

print 'Sorry '+popped_guest+' - I could not invite you after all!'

popped_guest=guest_list.pop()

print 'Sorry '+popped_guest+' - I could not invite you after all!'

popped_guest=guest_list.pop()

print 'Sorry '+popped_guest+' - I could not invite you after all!'

popped_guest=guest_list.pop()

print 'Sorry '+popped_guest+' - I could not invite you after all!'

print guest_list

# print message to the two persons still on list, let them know they're still invited

for guest in guest_list:
	print 'Hey,'+guest+". Contratulations! You're still invited - you lucky B6st6rd!"

# Use the 'del' Statement to remove the last two names of the list.
# print list to make sure and show the list is empty 

del guest_list[1]
del guest_list[0]

print guest_list

# list is empty ... finished!
