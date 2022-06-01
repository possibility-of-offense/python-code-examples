matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matrix_comprehension = [[ row[i] for row in matrix] for i in range(len(matrix) + 1)]

def custom_matrix_comprehension(l) :
    out = []

    for i in range(len(l) + 1) :
        temp = []
        for row in l :
            temp.append(row[i])

        out.append(temp)

    print(out)

custom_matrix_comprehension(matrix)