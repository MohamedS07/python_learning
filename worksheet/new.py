x = int(input("enter your mark = "))
if x <= 80 and x <= 100:
    print("A")
elif x <= 79 and x >= 60:
    print("B")
elif x <= 59 and x >= 50:
    print("C")
elif x <= 49 and x >= 40:
    print("D")
elif x < 40:
    print("Fail")

v = input("enter a character = ")
match v:
    case 'a'|'e'|'i'|'o'|'u':
            print("Vowels")
    case _:
            print("consonants")

age = int(input("enter the age = "))
if age < 5 :
    print("Free")
elif age <=12 and age >= 5:
    print("Ticket price is ",10)
elif age > 12 and age <= 64:
    print("Ticket price is ",20)
elif age >= 65 :
    print("Ticket price is ",15)
else:
    print("Invalid")


monthNumber = int(input("enter a month number = "))
match monthNumber:
        case 1:
            print("January")
        case 2:
            print("February")
        case 3:
            print("March")
        case 4:
            print("April")
        case 5:
            print("May")
        case 6:
            print("June")
        case 7:
            print("July")
        case 8:
            print("August")
        case 9:
            print("September")
        case 10:
            print("October")
        case 11:
            print("November")
        case 12:
            print("December")
        case _:
            print("Invalid month number")

