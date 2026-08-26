number = int (input ("Enter you number : "))

num1 = number
num2 = 0

while num1 != 0:
    last = num1 % 10
    num1 = num1 // 10
    num2 = num2*10 + last

print (f"Actual number : {number}")
print (f"reversed number : {num2}")

if number == num2:
    print ("The given number is Palindrome")
else:
    print ("The given number is not Palindrome")