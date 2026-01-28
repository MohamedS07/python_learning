# def character_string(content):
#     a = content[0]
#     b = content[-1]
#     print(a,b)

# character_string("Hello World")

# def vowels_count(sentence):
#     count = 0
#     if sentence == "":
#         print("Invalid")
#     else:
#         for i in sentence:
#             if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i or 'A' in i or 'E' in i or 'I' in i or 'O' in i or 'U' in i:
#                 count += 1
#         print(count)
            
# vowels_count("Hello World")
# vowels_count("")

# def word_count(word):
#     count = 1
#     for i in range(len(word)):
#         if word[i] ==" ":
#             count+=1
#     print(count)

# word_count("Hello World!!")

# def vowels_replace(replace):
#     result = ""
#     vowels = 'AEIOUaeiou'
#     for i in range(len(replace)):
#         if replace[i] in vowels:
#             result += '-'
#         else:
#             result += replace[i]
#     print(result)

# vowels_replace("Apple")


# def remove_vowels(word):
#     result = ""
#     vowels = 'AEIOUaeiou'
#     for i in range(len(word)):
#         if word[i] not in vowels:
#             result += word[i]
#     print(result)

# remove_vowels("Apple")

# def remove_numbers(word):
#     result = ""
#     num = '1','2','3','4','5','6','7','8','9','0'
#     for i in range(len(word)):
#         if word[i] not in num:
#             result += word[i]
#     print(result)

# remove_numbers("A12pp00le")

# def num_remove(word):
#     num = ['0','1','2','3','4','5','6','7','8','9']
#     result =""
#     for i in word:
#         if i not in num:
#             result += i
#     print(result)

# num_remove("He12llo Py00th55on")


# def reverse_word(sentence):
#     result = ""
#     word = ""
#     for i in sentence:
#         if i != " ":
#             word = i + word 
#         else:
#             result += word + " "
#             word = ""

#     result += word
#     print(result)

# reverse_word("Welcome to All")

# def letter_count(word,letter):
#     count = 0
#     for i in word:
#         if i == letter:
#             count += 1
#     print(count)

# letter_count("Mississippi",'s')

# def palindrome(content):
#     a =""
#     for i in range(len(content)-1,-1,-1):
#         a += content[i]

#     if a == content :
#         print("Yes")
#     else:
#         print("No")

# palindrome("Hello")
# palindrome("madam")


# def avg_numbers(numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     avg = total / len(numbers)
#     result = []
#     for num in numbers:
#         result.append(num - avg)

#     print(result)


# avg_numbers([10, 20, 30])


# def square_numbers(num):
#     s = []
#     for i in num:
#         s.append(i * i)
#     print(s)

# square_numbers([2, 3, 4, 5])


# def number_count(number,target):
#     count = 0
#     for i in number:
#         if i == target:
#             count += 1
#     print(count)

# number_count([3, 5, 3, 8, 3, 9],5)

def rem_minus_num(numbers):
    result = []
    for num in numbers:
        if num < 0:
            result.append(0)
        else:
            result.append(num)

    print(result)

rem_minus_num([5, -3, 9, -8, 2])
