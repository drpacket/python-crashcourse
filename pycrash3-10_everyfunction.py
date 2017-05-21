##################################################
##### 'Python Crash Course' Book - Exercises #####
##################################################

# 3-10. Every Function


# write program that creates a list of any! items, and
# then uses each function introduced in this chapter
# at least once ...

languages = ["ruby", "python", "java", "javascript", "html", "css", "php"]

print("Number of programing languages in the list: "+str(len(languages))+" languages")


def present_function(languages):
	for language in languages:
		print("\n" + language +" is another good language to learn")
	return languages

present_function(languages)

languages_sorted = sorted(languages)

print(languages_sorted)

print(sorted(languages, reverse=True))

# permanently sort

languages.sort()

print(languages)

languages.sort(reverse=True)

print(languages)

# IndexError

s = "ahjasduasd"

print(s[:4])

# deleting parts of a list with del and .pop()

print(languages_sorted)

# delete permanently with ***del LIST[index/slice]***

del languages_sorted[:2]

print(languages_sorted)

# use .pop() method to remove items from list, but still being able
# to store the "popped"/deleted list-item in a variable !

print(languages_sorted)

# Example: which of the prog.-languages in the list would you prefer to 
# learn first and foremost, with highest priority?


# make list with favorite languages and show restlist 
# Note: somehow i seemed to have the keen interest to make a function 
# with user-input out of it ;) 

def fav_languages(languages):
	print(languages)
	chosen = ""
	favorites = []
	while chosen != "exit":
		chosen = input('Choose your favorite language(s) from the list "languages".\n(Enter "EXIT" to finish)>').lower()
		for language in languages:
			if chosen == language:
				favorites.append(language)
				index = languages.index(language)
				del languages[index]
			elif languages == []:
				print("The original list is empty now!")
			else:
				break

	print(favorites)

	print("\nRemaining languages in the original list:\n")
	print(languages)
	return favorites




















