# string
# without importing you can use it

# lowercase
# uppercase
# sentence -> every word -> capitalize
# sentence -> beginning word -> capitalize

import string

content = "hello world"
print(content.capitalize())

left = "level"
right = "LEVEL"
print(right.casefold())

city = "JohnNESburg"
print(city.swapcase())

proverb = "practice makes man perfect"
print(proverb.upper())
print(proverb.title())

# dictionary