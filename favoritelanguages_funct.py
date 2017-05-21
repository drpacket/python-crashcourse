##################################################
##### 'Python Crash Course' Book - Exercises #####
##################################################

# NOTE: THIS FUNCTION IS A SPINNOF OF "EX.3-10. Every Function"

##################################################

# make list with favorite languages and show restlist 
# Note: somehow i seemed to have the keen interest to make a function 
# with user-input out of it ;) 

# original list (of programing languages)

languages = ["ruby", "python", "java", "javascript", "html", "css", "php"]

# function making new list of favorite languages with remainder of old input-list

def fav_languages(languages):
	print(languages)
	chosen = ""
	favorites = []
	while chosen != "exit":
		print("\nRemaining languages in list 'languages': ", languages, "\n")
		chosen = input('Choose your favorite language(s) from the list "languages".\n(Enter "EXIT" to finish)>').lower()
		for language in languages:
			if chosen.lower() == language:
				favorites.append(language)
				index = languages.index(language)
				del languages[index]
			elif languages == []:
				print("The original list is empty now\n")
				break
			else:
				continue

	print("Your preferred programming languagues:")
	print(favorites,"\n")

	print("Remaining languages in the original list:")
	print(languages,"\n")
	return favorites



# call function

fav_languages(languages)


