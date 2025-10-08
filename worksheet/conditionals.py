def calculator(operator,number1,number2):
    match operator:
        case '+':
            print(number1 + number2)
        case '-':
            print(number1 - number2)
        case '*':
            print(number1 * number2)
        case '/':
            print(number1 / number2)
        case _:
            print("invalid operator")

calculator('+',5,3)
calculator('-',10,4)
calculator('*',7,6)
calculator('/',20,5)
calculator('+', 20, 5)
calculator('-', 20, 5)


def max_of_three(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
max_of_three(3,5,10)
max_of_three(10,20,55)


def is_between(n, l, r):
    if n > l and n < r:
        print("yes")
    else:
        print("no")
is_between(3,2,6)
is_between(50,100,200)
is_between(50,20,200)