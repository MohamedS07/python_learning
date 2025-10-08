x = int(input("enter a x point = "))
y = int (input("enter a y point = "))
if x > 0 and y > 0 :
    print("Quadrant 1")
elif x < 0 and y > 0 :
    print("Quadrant 2")
elif x < 0 and y < 0 :
    print("Quadrant 3")
elif x > 0 and y < 0 :
    print("Quadrant 4")
elif x == y and y == x:
    print("same")
else:
    print("Invalid")

m = int(input("enter your rating = "))
match m :
    case 1:
        print("Very Bad")
    case 2:
        print("Bad")
    case 3:
        print("Average")
    case 4:
        print("Good")
    case 5:
        print("Excellent")
    case _:
        print("Invalid Rating")

n = int(input("Enter a number = "))
if n > 0:
    print("The number is positive")
elif n < 0:
    print("The number is negative")
elif n == 0:
    print("The number is zero")
else:
    print("Invalid")


v = input ("enter a character = ")
if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
        print("The character is a vowel")
elif v == 'A' or v == 'E' or v == 'I' or v == 'O' or v == 'U':
        print("The character is a vowel")
else:
        print("The character is a consonant")

t = int(input("Total purchase = "))
s = (t//10)
m = bool(int(input("your are a member (true/false) = ")))
if m == 1:
    print("you got a reward points is",s,"point")
elif m == 0:
    print("not member")
else:
    print("Invalid")


def dl_method(team_score, target_score, overs_left):
    # Enter your code here
    if team_score >= target_score:
        print("Team wins by DL method")
    elif team_score < target_score and overs_left > 0:
        print("Match to be continued")
    elif team_score < target_score and overs_left == 0:
        print("Team loses by DL method")



