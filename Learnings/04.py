number = int (input ("Enter your number : "))

num1 = number
result = 0
digits = len (str (number))

while num1 != 0:
    last = num1 % 10
    result = result + last ** digits
    num1 = num1 // 10

if number == result:
    print (f"Result : {result}, The given number is Armstrong number")
else:
    print (f"Result : {result}, The given number isn't Armstrong number")