def binarySearch(arr, v):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) // 2

        if arr[m] == v:
            return True
        
        if arr[m] < v:
            l = m + 1
        else:
            r = m - 1

    return False

# myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# myTarget = 15

# result = binarySearch(myArray, myTarget)

# if result != -1:
#     print("Value",myTarget,"found at index", result)
# else:
#     print("Target not found in array.")

print(binarySearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19],15))
