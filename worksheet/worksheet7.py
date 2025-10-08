def sum_of_num (a,b):
    while a <= b:
        print(a)
        a = a + 1
sum_of_num (10,20)

question 2

def num_of_sum (a,b,n):
    count = 0
    if n <= 0:
        print('Invalid')
    else:
        for i in range (a , b + 1):
            if i % n == 0:
                count = count + 1
        print(count)

num_of_sum (10,20,0)
num_of_sum (10,20,3)
num_of_sum (10,30,4)
num_of_sum (10,20,2)




w = int(input())

a =  w // 1000 * 5
b =  w // 5000 * 20
t = a + b
print(t)
    







 
