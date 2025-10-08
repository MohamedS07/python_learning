#1
a = int(input('Enter a Year = '))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print('Y')
else:
    print('N')


#2
a = int(input('Enter a first number = '))
b = int(input('Enter a second number = '))
c = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        c = c + i
print(c)


#3
x = int(input('Enter the kilograms = '))
if x <= 5 :
    print ( 10 * 1.05)
elif x > 5 and x <= 20:
    print( 20 * 1.05)
elif x > 20:
    print(50 * 1.05)

#4
marks = int(input('Enter a number = '))
if marks == 100:
    print("S")
elif marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
elif marks >= 50:
    print("E")
else:
    print("F")

#5
f = input('Enter a Food P / B / S = ')  
q = int(input('Quantity = '))  
if f == "P":
        t = q * 200
        print(t * 1.05)
elif f == "B":
        t = q * 100
        print(t * 1.05)
elif f == "S":
        t = q * 50
        print(t * 1.05)
elif q < 0:
        print("Invalid Input")
