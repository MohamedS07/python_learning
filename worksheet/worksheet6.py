1
age = int(input("Enter age: "))

if age < 18:
    print(150)
elif age <= 18 or age <= 60:
    print(250)
else:
    print(100)

2
age = int(input("Enter age: "))

if age < 12:
    ticket = 50
    if age % 2 == 0:
        ticket -= 5
    print(ticket)
elif age <= 59:
    ticket = 120
    if age % 2 == 0:
        ticket -= 5
    print(ticket)
elif age >= 60:
    ticket = 80
    if age % 2 == 0:
        ticket -= 5
    print(ticket)

#3
n = int(input("Enter number of mangoes: "))

if n >= 0:
    print("Full Basket is", n // 5)
    print("Left Over mangoes is", n % 5)

#4
n = int(input("Enter number of candies: "))

if n > 0:
    for day in range(1, n+1):
        print("Day", day, "=", n-day, "left")

# #5
salary = int(input("Enter your salary: "))
sales = int(input("Enter your sales: "))

if sales >= 100:
    print("Bonus =", int(salary * 0.10))
    print("Total Salary =", int(salary + salary * 0.10))

elif sales >= 50:
    print("Bonus =", int(salary * 0.05))
    print("Total Salary =", int(salary + salary * 0.05))

else:
    print("Bonus = 0")
    print("Total Salary =", salary)

#6
sales = int(input("Enter weekly sales: "))

if sales <= 5000:
    print(int(sales * 0.05))
elif sales <= 10000:
    print(int(sales * 0.10))
else:
    print(int(sales * 0.15))

#7
price = int(input("Enter price: "))

if price > 100:
    print(int(price - price * 0.10))
elif price >= 50:
    print(int(price - price * 0.05))
else:
    print(price)

#8
ext = input("Enter file extension: ")

if ext == ".csv":
    print("This is an Excel File")
elif ext == ".jpg":
    print("This is a JPEG File")
elif ext == ".doc":
    print("This is a Word File")
elif ext == ".pdf":
    print("This is a PDF File")
elif ext == ".py":
    print("This is a Python File")
else:
    print("Unknown File Type")
# 9
km = int(input("Enter distance in km: "))

if km <= 10:
    print(km * 15)
elif km <= 30:
    print((10 * 15) + (km - 10) * 12)
else:
    print((10 * 15) + (20 * 12) + (km - 30) * 10)

# # 10
n = int(input("Enter Lily's age: "))

toys = 0
money = 0
amount = 10

if n > 0:
    for age in range(1, n+1):
        if age % 2 == 1:   # odd birthday
            toys += 1
        else:              # even birthday
            money += amount - 1
            amount += 10

    print(toys)
    print(f"{money:.2f}")





