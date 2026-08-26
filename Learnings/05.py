number = int (input ("Enter your number : "))

# method 1 : TC O(n)
result1 = []

for i in range (1, number + 1):
    if number % i == 0:
        result1.append (i)

print (f"The number you have given is divisible by : {result1}")

# method 2 : TC O(N)
result2 = []

for i in range (1, (number // 2) + 1):
    if number % i == 0:
        result2.append (i)
result2.append (number)

print (f"The number you have given is divisible by : {result2}")

# method 3 : TC O(root(N))
result3 = []

for i in range (1, int (number ** (1/2)) + 1):
    if number % i == 0:
        result3.append (i)
        if number // i != i:
            result3.append (number // i)

print (f"the number you have given is divisible by : {result3}")