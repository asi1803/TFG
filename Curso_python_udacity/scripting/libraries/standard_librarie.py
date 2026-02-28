# use the math module
# print e to the power of 3 using the math module

import math
print(math.exp(3))

# %%
# Todo: First import the `random` module

# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Todo: Add your function generate_password below
# It should return a string consisting of three random words 
# concatenated together without spacesç
import random
def generate_password():
	# use random.choice() to select three random words from word_list
	word1 = random.choice(word_list)
	word2 = random.choice(word_list)
	word3 = random.choice(word_list)
	# concatenate the three words together and return the result
	password = word1 + word2 + word3
	return password

# Now we test the function
print(generate_password())
