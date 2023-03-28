programing_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary
# print(programing_dictionary["Bug"])

# Adding new items to dictionary
programing_dictionary["Loop"] = "The action of doing something over and over again."
# other way to add new items to dictionary
programing_dictionary.update({"Class": "A user-defined prototype for an object that defines a set of attributes that characterize any object of the class."})
# other way to add new items to dictionary
print(programing_dictionary)


# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"]
} 
# Nesting Dictionary in a Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10
    }
} 

# Nesting Dictionary in a List
travel_log = [
   {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
   { 
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10
    }
]