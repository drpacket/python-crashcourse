##################################################
##### Python Crash Course - Classes ##############
##################################################

# 9-1.Restaurant  

##################################################

class Restaurant:
    """Model for simple Restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Name:", self.restaurant_name, "\nCuisine:", self.cuisine_type, "\n")

    def open_restaurant(self):
        print(str(self.restaurant_name) + " is now open!\n", )
    
restaurant = Restaurant("Carlitos", "Italian")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

print("-------------------------------------------------")
# 9-2.Three Restaurants

restaurant.describe_restaurant()
restaurant.open_restaurant()

french_restaurant = Restaurant("Henrys", "French")
steakhouse = Restaurant("Assado Steak", "Steakhouse")

french_restaurant.describe_restaurant()
steakhouse.describe_restaurant()

print("-------------------------------------------------")
# 9-3. Users

class User:
    """Template to create User Profiles"""
    def __init__(self, first_name, last_name, added, status):
        self.first_name = first_name
        self.last_name = last_name
        self.added = added
        self.status = status
    def describe_user(self):
        print("\nUser: " + self.last_name + ", " + self.first_name + ". " + "Date added: " + self.added \
        + ". " "Member status: " + self.status)
    def greet_user(self):
        print("\nHello, " + self.last_name + " " + self.first_name + "." + " Welcome to our club!")

franco = User("Frank", "Gottinger", "June 2nd", "member")
michael = User ("Michael", "Corleone", "Dec 24th", "applicant")
jimmy = User("Jimmy", "Two-Face", "Sept 13th", "honorary member")

print("-------------------------------------------------")

franco.describe_user()
franco.greet_user()

michael.describe_user()
michael.greet_user()

jimmy.describe_user()
jimmy.greet_user()

print("-------------------------------------------------")


# --- EOF ---
##################################################