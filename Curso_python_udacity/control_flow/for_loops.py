# Write a for loop to print out each word in the sentence list, one word per line
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for word in sentence:
    print(word)

print("\n")
#Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.
for num in range (0, 31, 5):
    print (num)

#EJERCICIO
#Write a for loop that iterates over the names list to create a usernames list. 
# To create a username for each name, make everything lowercase and replace spaces with underscores. 
# Running your for loop over the list:
#HINT: Use the .replace()(opens in a new tab) method to replace the spaces with underscores.

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
# write your for loop here

for name in names:
    usernames.append(name.lower().replace(" ", "_"))
print(usernames)
#otra opción
for name in names:
   name = name.lower().replace(" ", "_")
print(names)

#Write a for loop that uses range() to iterate over the positions in usernames to modify the list. 
# Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores.
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")
print(usernames)


#EJERCICIO TAG COUNTER
#Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags
#XML is a data language similar to HTML.
#You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". 
#Keep track of the number of tags using the variable count.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token.startswith("<") and token.endswith(">"):
        count += 1

print(count)

#EJERCICIO HTML LIST
#Write some code, including a for loop,
#that iterates over a list of strings and creates a single string, html_str, 
#which is an HTML list

items = ['first string', 'second string']
html_str = "<ul>\n"  
# "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)