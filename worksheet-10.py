def vowel_find(content):
    l = []
    for i in content:
        if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i :
                l += i
    print(l)

vowel_find('education')

def max_vowels(word):
    v = 'aeiou'
    for i in word:
        if i not in v:
            i = max(word)
    print(i)

max_vowels(["cat", "eagle", "umbrella", "sky"])


def odd_even_count(num):
    d = {}
    count_1 = 0
    count_2 = 0
    for i in num:
        if i % 2 == 0:
            count_1 += 1
        else:
            count_2 += 1
        d["even"] = count_1
        d["odd"] = count_2
    print(d)
odd_even_count([1, 2, 3, 4, 5, 6, 7])


nums = [2, 4, 6, 4, 8, 4, 10]
target = 4

first = -1
last = -1

for i in range(len(nums)):
    if nums[i] == target:
        if first == -1:     
            first = i
        last = i            

result = {"first_index": first, "last_index": last}
print(result)


def combine_list(n,m):
    new=[]
    for i in range(0,len(n)):
        new.append(n[i])
        new.append(m[i])
    print(new)
combine_list([10, 20, 30],[1, 2, 3])


