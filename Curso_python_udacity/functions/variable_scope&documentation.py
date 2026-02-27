# This works fine
#word = "hello"
#def some_function():
#    print(word)

#some_function()
#Notice that we can still access the value of the global variable `word` within this function. However, the value of a global variable can not be __modified__ inside the function. If you want to modify that variable's value inside this function, it should be passed in as an argument. You'll see more on this in the next quiz.
#Scope is essential to understanding how information is passed throughout programs in Python and really any programming language.

# %%
# Ejemplo de documentación de funciones
def population_density(population, land_area):
    """Calculate the population density of an area. 
    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.
    OUTPUT: 
    population_density: population / land_area. The population density of a particular area."""
    return population / land_area
# %%

def readable_timedelta(days):
    # insert your docstring here
    """ Convert a number of days to a string that represents number of weeks and number of days."""
    
    #otra forma de escribir la docstring
    """Return a string of the number of weeks and days included in days.
    
    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days"""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)