def zeroMatrix(matrix):
    rows = {i : False for i in range(len(matrix))}
    columns = {i : False for i in range(len(matrix[0]))}

    for rowIndex in range(len(matrix)):
        for colIndex in range(len(matrix[rowIndex])):
            if matrix[rowIndex][colIndex] == 0:
                rows[rowIndex] = True
                columns[colIndex] = True

    for rowIndex in range(len(matrix)):
        for colIndex in range(len(matrix[rowIndex])):
            if rows[rowIndex] or columns[colIndex]:
                matrix[rowIndex][colIndex] = 0

    return matrix

def printMatrix(matrix):
    for row in matrix:
        print(row)
    return None

ex1 = [[1, 0], [1, 1]]
ex2 = [[0, 0, 1], [1, 1, 1], [2, 3, 4]]
ex3 = [[0, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 0], [4, 4, 0, 4]]
