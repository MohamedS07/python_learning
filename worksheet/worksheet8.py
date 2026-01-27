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



    


