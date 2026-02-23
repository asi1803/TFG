a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

#What would the output of the following code be? (Treat the comma in the multiple choice answers as newlines.)
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

#What would the output of the following code be? (Treat the comma in the multiple choice answers as newlines.)
names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))

#What would the output of the following code be? (Treat the comma in the multiple choice answers as newlines.)
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# print ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(arr[:])

#print(['a', 'b', 'c'])
print(arr[3:])

# print ['c', 'd', 'e', 'f']
print(arr[2:6])