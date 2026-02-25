
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here

    # multiply the product so far by the current number
    # increment current with each iteration until it reaches number
while current<= number:
    product *= current
    current += 1
    print(product)

# print the factorial of number
print(product)

# %%
# Mismo ejercicio pero con un for loop

number =6
product =1 
current = 1

for current in range (1, number + 1):
    product *= current

print(product)

# %%

#Ejercicio

start_num = 1 #provide some start number
end_num = 700#provide some end number that you stop when you hit
count_by = 3#provide some number to count by 

break_num = start_num
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num

while break_num < end_num:
    print(break_num)
    break_num += count_by
print(break_num)

# %%
start_num = 00 #provide some start number
end_num = 700 #provide some end number that you stop when you hit
count_by = 3#provide some number to count by 
# write a condition to check that end_num is larger than start_num before looping

if end_num <= start_num:
        result = "Oops! Looks like your start value is greater than the end value. Please try again."
else:
     break_num = start_num
     while break_num < end_num:
        break_num += count_by

     result = break_num

print(result)
# %%
# Ejercicio para encontrar el cuadrado más cercano a un número dado
limit = 40
nearest_square = 0
i=0
# write your while loop here
while (i+1)**2 < limit:
     i += 1
     nearest_square = i**2

print(nearest_square)
    
