# 1 question

N = int(input('Enter a first number :'))
M = int(input('Enter a second number :'))
s = (N + M)
if s % 2 == 0:
    print('Even')
else:
    print('Odd')

2 question

a = int(input('Enter a number:'))
b = a // 10
c = a % 10
d = b + c
e = b * c
if d + e == a :
    print('Great')
else :
    print('Not Great')


3 question

consumer = input('What kind of consumer (residential/commercial): ')
unit = int(input('Enter units : '))
if consumer == 'residential':
    if unit <=100 and unit > 0:
        print('Total unit amount is =', 3*unit)
    elif unit <=200 and unit > 100:
        print('Total unit amount is =', 5*unit)
    elif unit > 200:
        print('Total unit amount is =' ,7*unit)

elif consumer == 'commercial':
    if unit <=100 and unit > 0:
        print('Total unit amount is =', 5*unit)
    elif unit <=200 and unit > 100:
        print('Total unit amount is =', 7*unit)
    elif unit > 200:
        print('Total unit amount is =' ,10*unit)


#4 question

a = int(input('Enter a distance:'))
b = 50
if a >= 0 and a <= 5 :
    print(b, 'rupees')
elif a >= 6 and a <= 15 :
    print(a * 8, 'rupees')
elif a > 15 :
    print(a * 6, 'rupees')
else :
    print('Invalid input')


#5 question

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c and c == a:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")

#6 question

a = int(input('Enter a number = '))
if a % 3 == 0 and a % 5 == 0:
    print('FizzBuzz')
elif a % 3 == 0:
    print('Fizz')
elif a % 5 == 0:
    print('Buzz')
else:
    print('The number is not divisible')

#7 question

e = input('Enter a course (Science / Commerce / Arts ) = ')
match e:
    case 'Science':
        s = input('Choose your course = ')
        match s:
            case 'Medical':
                print('Choose path : Science -> Medical')
            case 'Engineering':
                print('Choose path : Science -> Engineering')
            case _:
                print('Invalid Subject')
    case 'Commerce':
        s = input('Choose your course = ')
        match s:
            case 'CA':
                print('Choose path : Commerce -> CA')
            case 'B.com':
                print('Choose path : Commerce -> B.com')
            case _:
                print('Invalid Subject')
    case ' Arts':
        s = input('Choose your course = ')
        match s:
            case 'History':
                print('Choose path :  Arts -> History')
            case 'Literature':
                print('Choose path :  Arts -> Literature')
            case _:
                print('Invalid Subject')

#8 question

show = int(input('Enter a timing = '))
if show >= 9 and show <= 12:
    print('Morning Show')
elif show > 12 and show <=16:
    print('Matinee Show')
elif show > 16 and show <= 20:
    print('Evening Show')
elif show > 20 and show <=24:
    print('Night Show')
else:
    print('Invalid Timing')

9 question
  
kilometer = float(input('Enter the distance in kilometer = '))
convert = input('What type of conversion ( m / mm / cm / mi ) = ')

match convert:
    case 'm':
        print(kilometer*1000,'m')
    case 'mm':
        print(kilometer*1000000,'mm')
    case 'cm':
        print(kilometer*100000,'cm')
    case 'mi':
        print(kilometer*0.621371,'miles')
    case _ :
        print('Invalid Conversion')

10 question

pay = input('Enter Payment Mode ( UPI / Card / Net Banking / COD ) = ')
if pay == "UPI":
    print("You selected UPI payment")
elif pay == "Card":
    print( "You selected Debit/Credit Card payment")
elif pay == "Net Banking":
    print("You selected Net Banking")
elif pay == "COD":
    print("You selected Cash on Delivery")
else:
    print("Invalid Payment Mode")