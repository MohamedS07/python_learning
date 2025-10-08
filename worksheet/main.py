v = int(input("enter your age = "))
if v <= 100 and v >= 18:
    print("you are eligible to vote")
elif v <= 17 and v >= 1:
    print("you are not eligible to vote")
else:
    print("Invalid")


t = int(input("enter the temperature = "))
if t < 20 :
    print("Cold")
elif t < 30 and t >= 20 :
    print("Warm")
elif t < 30 :
    print("Hot")
