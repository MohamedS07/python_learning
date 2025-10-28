# Activity  1

fruits = ("apple", "banana", "cherry", "mango", "banana")

# Address the following:

# 1.Determine the length of the fruits tuple.

print(len(fruits))

# 2.Identify the index of the initial occurrence of "banana".

print(fruits.index("banana"))

# 3.Attempt to modify "cherry" to "grape" within the tuple. Explain the outcome and the reason behind it.

a = list(fruits)
a[2] = "grape"
fruits = tuple(a)
print(fruits)

'''
We cannot directly modify the tuple . but we use list to modify the tuple 
'''
# 4.Transform the tuple into a list, make a modification, and then convert it back to a tuple.

a = list(fruits)
a[4] = "cherry"
fruits = tuple(a)

print(fruits)

# Activity 2

colors = ("red", "green", "blue")
shapes = ("circle", "square", "triangle")

# Perform the following operations

# Combine colors and shapes to create a new tuple called art.

art = colors + shapes
print(art)

# Demonstrate how to repeat a tuple, specifically colors three times.

print(colors * 3)

# add Diamond element
j = "Diamond"
art = art + (j,)
print(art)


# Extract and print the middle element from the art tuple using slicing.

a = int(len(art) // 2)
b = art[a]
print(b)

# Verify if the string "square" exists within the art tuple.

if 'square' in art:
    print('Yes, The square is in the tuple')
else:
    print('No, The square not in the tuple')


# Activity 3

marks = (78, 85, 69, 90, 85)

# Determine the highest and lowest marks.

a = max(marks)
b = min(marks)
print("Highest mark:", a)
print("Lowest mark:", b)

# Count the occurrences of the mark 85.

c = marks.count(85)
print("Occurrences of 85:", c)

# Calculate the average marks using the sum() and len() functions.

average = sum(marks) / len(marks)
print("Average marks:", average)

# Activity 4

monthly_rainfall = (120, 150, 120, 180, 120, 90, 110, 130, 100, 140, 120, 160)

# Calculate the total annual rainfall.

total = sum(monthly_rainfall)
print("Total annual rainfall:", total)

# Determine the average monthly rainfall.

average = total / len(monthly_rainfall)
print("Average monthly rainfall:", average)

# Identify the month(s) with exactly 120 mm of rainfall. (Hint: Consider using enumerate() or .count().

months_with_120 = [i for i, rain in enumerate(monthly_rainfall) if rain == 120]
print("Indices of months with 120 mm:", months_with_120)
print("Count of such months:", monthly_rainfall.count(120))

# Find the highest and lowest rainfall values recorded.

a = max(monthly_rainfall)
b - min(monthly_rainfall)
print("Highest rainfall:", a)
print("Lowest rainfall:", b)





