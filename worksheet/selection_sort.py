def selection_sort(sort):
    if sort == []:
        print("Invalid")
    else:
        for i in range(len(sort)-1):
            m = i
            for j in range(i+1,len(sort)):
                if sort[j] < sort[m]:
                    sort[m] = sort[i+1]
                    # temp = sort[m]
                    # sort[m] = sort[i]
                    # sort[i] = temp

                    return sort

print(selection_sort([64, 34, 25, 5, 22, 11, 90, 12]))