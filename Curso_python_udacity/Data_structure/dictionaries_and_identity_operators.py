# Define a Dictionary, population,
# that provides information on the world's largest cities The key is the name of a city
# (a string), and the associated value is its population in millions of people.
#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5
population = {'Shanghai': 17.8,'Istanbul': 13.3,'Karachi': 13.0,'Mumbai': 12.5}
# Define a variable, city, and assign it the value 'Istanbul'.
city = 'Istanbul'
# Use the in operator to check if city is a key in the population dictionary.
city in population
# Use the in operator to check if 'Istanbul' is a key in the population dictionary
'Istanbul' in population
# Use the in operator to check if 'Mumbai' is a key in the population dictionary
'Mumbai' in population

#What will the output of the following code be?
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)
# The output will be:
# a and b are equal because they have the same contents, so a == b will print True.
# a and b are the same object in memory, so a is b will print True.
# a and c are equal because they have the same contents, so a == c will print True.
# a and c are different objects in memory, so a is c will print False.

animals = {'dogs': [20, 10, 15, 8, 32, 15], 
 'cats': [3,4,2,8,2,4], 
 'rabbits': [2, 3, 3], 
 'fish': [0.3, 0.5, 0.8, 0.3, 1]}
#The data type of the keys in the dictionary animals is string, and the data type of the values is list.
# The keys are 'dogs', 'cats', 'rabbits', and 'fish', and the values are lists of numbers representing the counts of each type of animal.
#The result of animals['dogs'] will be the list [20, 10, 15, 8, 32, 15], which represents the counts of dogs in the dictionary.
#The result of animals['dogs'][3] will be the number 8, which is the fourth element in the list of dog counts (since indexing starts at 0).

# invalid dictionary - this should break
room_numbers = {['Freddie', 'Jen']: 403,
    ['Ned', 'Keith']: 391,
    ['Kristin', 'Jazzmyne']: 411,
    ['Eugene', 'Zach']: 395}
# The above code will raise a TypeError because lists cannot be used as keys in a dictionary.
