# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)

# this returns something
def add_ten(num):
    return(num + 10)

print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))

# %%
# Write a function named population_density that takes two arguments, 
# population and land_area, and returns a population density calculated from those values
# write your function here
def population_density(population, land_area):
    return population / land_area


# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))
# %%

# write your function here

def readable_timedelta(days):
    remaining_days = days % 365
    weeks = remaining_days // 7
    remaining_days = remaining_days % 7
    return '{} week(s), and {} day(s)'.format(weeks,remaining_days)

# test your function
print(readable_timedelta(50))
# %%
