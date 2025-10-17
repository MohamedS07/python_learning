#1
def greater_than(a, num):
    sum = 0
    for i in a:
        if i > num :
            sum += i
    print(sum)
    
greater_than([2, 3, 1, 4, 5],2)

#2
def odd_numbers(num):
    for i in num:
        if i % 2 != 0:
            print(i)

odd_numbers([22,23,77,45])
odd_numbers([34,10,49,76])