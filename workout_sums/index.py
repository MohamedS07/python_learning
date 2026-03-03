def new_array(li):
    a = []
    for i in li:
        if i not in a:
            a.append(i)
    print(a)

new_array([1,2,2,3,4,4,4,5,6,6,6,6])


def adding_matrix(matrix_1,matrix_2):
    for i in range(len(matrix_1)):
        li = []
        for j in range(len(matrix_1[0])):
            li.append(matrix_1[i][j] + matrix_2[i][j])
        print(li)

adding_matrix(([1, 2, 3],[4, 5, 6]),([7, 8, 9],[1, 0, 1]))

