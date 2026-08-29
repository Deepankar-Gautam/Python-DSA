x = int (input ("Digits in your array : "))
array = []
for i in range (0, x):
    y = int (input (f"Enter your input {i + 1} : "))
    array.append (y)

# method 1 : TC O(N)
dict = {}

for i in range (0, len (array)):
    if array [i] in dict:
        dict [array [i]] = dict [ array [i]] + 1
    else:
        dict [array [i]] = 1

print (array)
print (dict)

# method 2 : TC O(N)
hash_map = {}

for i in range (0, len (array)):
    hash_map [array [i]] = hash_map.get (array [i], 0) + 1

print (hash_map)
