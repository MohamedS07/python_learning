x = 5
y = 2

print(x > y)
print(x < y)
print(x == y)
print(x >= y)
print(x <= y)
print(x != y)

#odd or even
n = int(input("Enter a value of n = "))
print (n)
if n%2 == 0 :
    print("even")
else:
    print("odd")

#leap year or not
n = int(input("Enter a year = "))
print (n)
if n%4 == 0 :
    print(n,"it's a leap year")
else:
    print(n,"it's not a leap year")


#divisible or not
d = int(input("Enter a number = "))
print (d)
if d%3 == 0 or d%5 == 0 :
    print(d,"the given number is divisible")
else:
    print(d,"the given number is not divisible")


#century or not
a = int(input("Enter a year = "))
if a >= 2001 and a <= 2100:
    print(a,"it's a 21st century")
else:
    print(a,"it's not a 21st century")





