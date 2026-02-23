new_str = "The cow jumped over the moon."
new_str.split()
print (new_str.split())
#Output is:
#['The', 'cow', 'jumped', 'over', 'the', 'moon.']```

#2. Here  the separator is space, and the maxsplit argument is set to 3.
new_str.split(' ', 3)
print (new_str.split(' ', 3))
#Output is:
#['The', 'cow', 'jumped', 'over the moon.']```

#3. Using '.' or period as a separator.
new_str.split('.')
print (new_str.split('.'))
#Output is:
#['The cow jumped over the moon', '']

#4. Using no separators but having a maxsplit argument of 3.
new_str.split(None, 3)
print (new_str.split(None, 3))
#Output is:
#['The', 'cow', 'jumped', 'over the moon.']```