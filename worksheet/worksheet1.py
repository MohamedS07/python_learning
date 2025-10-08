t = int(input("enter your tamil mark = "))
e = int(input("enter your english mark = "))
m = int(input("enter your maths mark = "))

if t > 40 and e > 40 and m > 40:
    print("promoted")
else:
    print("not promoted")

w = input("enter weather condition today = ")

if w == "rainy" or w == "sunny":
    print("bring umbrella")
else:
    print("no umbrella needed")


d = input("enter the day = ")

if d == "saturday" or d == "sunday":
    print("holiday")
else:
    print("working day")


