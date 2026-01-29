# 1

def character_string(content):
    a = content[0]
    b = content[-1]
    print(a,b)

character_string("Hello World")

2

def vowels_count(sentence):
    count = 0
    if sentence == "":
        print("Invalid")
    else:
        for i in sentence:
            if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i or 'A' in i or 'E' in i or 'I' in i or 'O' in i or 'U' in i:
                count += 1
        print(count)
            
vowels_count("Hello World")
vowels_count("")

3

def word_count(word):
    count = 1
    for i in range(len(word)):
        if word[i] ==" ":
            count+=1
    print(count)

word_count("Hello World!!")

4

def vowels_replace(replace):
    result = ""
    vowels = 'AEIOUaeiou'
    for i in range(len(replace)):
        if replace[i] in vowels:
            result += '-'
        else:
            result += replace[i]
    print(result)

vowels_replace("Apple")

5

def remove_vowels(word):
    result = ""
    vowels = 'AEIOUaeiou'
    for i in range(len(word)):
        if word[i] not in vowels:
            result += word[i]
    print(result)

remove_vowels("Apple")

6

def remove_numbers(word):
    result = ""
    num = '1','2','3','4','5','6','7','8','9','0'
    for i in range(len(word)):
        if word[i] not in num:
            result += word[i]
    print(result)

remove_numbers("A12pp00le")

7

def num_remove(word):
    num = ['0','1','2','3','4','5','6','7','8','9']
    result =""
    for i in word:
        if i not in num:
            result += i
    print(result)

num_remove("He12llo Py00th55on")

8

def reverse_word(sentence):
    result = ""
    word = ""
    for i in sentence:
        if i != " ":
            word = i + word 
        else:
            result += word + " "
            word = ""

    result += word
    print(result)

reverse_word("Welcome to All")

9

def letter_count(word,letter):
    count = 0
    for i in word:
        if i == letter:
            count += 1
    print(count)

letter_count("Mississippi",'s')

10

def palindrome(content):
    a =""
    for i in range(len(content)-1,-1,-1):
        a += content[i]

    if a == content :
        print("Yes")
    else:
        print("No")

palindrome("Hello")
palindrome("madam")

11

def avg_numbers(numbers):
    total = 0
    for i in numbers:
        total += i
    avg = total / len(numbers)
    result = []
    for num in numbers:
        result.append(num - avg)

    print(result)


avg_numbers([10, 20, 30])

12

def square_numbers(num):
    s = []
    for i in num:
        s.append(i * i)
    print(s)

square_numbers([2, 3, 4, 5])

13

def number_count(number,target):
    count = 0
    for i in number:
        if i == target:
            count += 1
    print(count)

number_count([3, 5, 3, 8, 3, 9],5)

14

def rem_minus_num(numbers):
    result = []
    for num in numbers:
        if num < 0:
            result.append(0)
        else:
            result.append(num)

    print(result)

rem_minus_num([5, -3, 9, -8, 2])

15

def count_greatest(num):
    count = 0
    for i in num:
        if i > 50:
            count += 1
    print(count)

count_greatest([20, 60, 75, 45, 90, 35])

16

def first_last_sum(number):
    a = number[0]
    b = number[-1]
    c = a + b
    print(c)

first_last_sum([10, 20, 30, 40, 50])

17

def find_index(fruits):
    for i in range(len(fruits)):
        print("Index", i, fruits[i])

find_index(["apple", "banana", "grapes"])

18

def add_odd_even(numbers):
    list_1 = []
    list_2 = []
    for i in numbers:
        if i % 2 == 0:
            list_1.append(i)
        else:
            list_2.append(i)

    a = sum(list_1)
    b = sum(list_2)

    print("even_sum = ",a, "odd_sum = ",b)

add_odd_even([10, 15, 20, 25, 30])

19

def rem_minus_num(numbers):
    result = []
    for num in numbers:
        if num < 0:
            result.append(0)
        else:
            result.append(num)

    print(result)

rem_minus_num([10, -5, 20, -10, 30])

20

def find_list(main_list, sub_list):
    found = False
    for i in range(len(main_list) - len(sub_list) + 1):
            if main_list[i:i + len(sub_list)] == sub_list:
                    found = True

    print(found)



find_list([1, 2, 3, 4, 5, 6], [3, 4, 5])
find_list([1, 2, 3, 4, 5, 6], [2, 4, 6])

21

def check_word(s1,s2):
    if len(s1) == len(s2) and s2 in (s1 + s1):
        print(True)
    else:
        print(False)

check_word("ABCDE","CDEAB")

22

def ignore_last(arr,k):
    for i in range(len(arr)-k):
            print(arr[i])

ignore_last([10, 20, 30, 40, 50],1)

23

def add_numbers(numbers):
    a = 0
    for i in range (len(numbers)-1):
        a += numbers[i] + numbers[i + 1]
    print(a)

add_numbers([1,2,3,4,5])

24

def number_count(nums,k):
    count = 0
    for i in nums:
        if i == k:
            count += 1
    print(count)

number_count( [4, 1, 1, 4, 2, 4, 3, 1, 5],4)
    
