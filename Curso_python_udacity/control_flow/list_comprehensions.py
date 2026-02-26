#capitalized_cities = []
#for city in cities:
#    capitalized_cities.append(city.title())
#can be reduced to:
#capitalized_cities = [city.title() for city in cities]

#You can also add conditionals to list comprehensions (listcomps). 
#After the iterable, you can use the if keyword to check a condition in each iteration.
#squares = [x**2 for x in range(9) if x % 2 == 0] --> solo para numeros pares

#If you would like to add else, you have to move the conditionals to the beginning of the listcomp:
#squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]

# %%
#Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)
# %%
# use a list comprehension to create a list of the first 20 multiples of 3 

multiples_3 = [x * 3 for x in range(1,21)]
print(multiples_3)
# %%
# Use a list comprehension to create a list of names passed that only include those that scored at least 65.

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)
