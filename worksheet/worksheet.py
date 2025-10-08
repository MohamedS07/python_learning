t = int(input("Enter a value given by thara = "))
j = int(input("Enter a value given by jyothi = "))

if (t & j)%5 ==0:
    print(1)
else:
    print(0)

n = int(input("Enter the number = "))
if n%7 ==0:
    print('yes')
else:
    print('no')


amount = int(input("Enter a amount = "))
c = 50
if amount > 500 :
    print('Free Delivery.')
else:
    print(amount,'+',c,'rupees extra charged')


x = int(input("Enter your grade = "))

if 80 <= x <= 100:
    print("A")
elif 60 <= x <= 79:
    print("B")
elif 50 <= x <= 59:
    print("C")
elif 40 <= x <= 49:
    print("D")
elif x < 40:
    print("Fail")

a = int(input("Enter the first value = "))
b = int(input("Enter the second value = "))
c = int(input("Enter the third value = "))
if a + b and a + c and b + c:
    print("yes")
else:
    print("no")


age = int(input("Enter your age = "))

if age < 13:
    print("Child")
elif 13<= age <= 19:
    print("Teen")
elif 20<= age <= 59:
    print("Adult")
elif 60<= age <= 100:
    print("Senior")
else:
    print("Invalid")

