def rotateMatrix(matrix):
    for layer in range(len(matrix) / 2):
        rotateLayer(matrix, layer, len(matrix) - 1 - layer)
    return matrix

def rotateLayer(matrix, first, last):
    for index in range(first, last):
        offset = index - first
        # Save values
        top = matrix[first][index]
        right = matrix[index][last]
        bottom = matrix[last][last - offset]
        left = matrix[last - offset][first]
        # Reassign values
        matrix[first][index] = left
        matrix[index][last] = top
        matrix[last][last - offset] = right
        matrix[last - offset][first] = bottom
    return None

def printMatrix(matrix):
    for row in matrix:
        print(row)
    return None

example2 = [[1, 2], [3, 4]]
example3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
example4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
example5 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
