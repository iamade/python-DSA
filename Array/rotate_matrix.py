'''
Rotate Matrix/ Image - LeetCode 48

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.

    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

'''

def rotate(matrix):
    n = len(matrix)
    #Transpose the matrix
    #Iterate over the rows
    for i in range(n):
        #Iterate over the columns starting from the current row 'i'
        for j in range(i, n):
             #Swap the elements at positions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

     # Reverse each row
            # Iterate over each row in the matrix
    for row in matrix:
        #Reverse the elements in the current row
        row.reverse()       

    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))

'''
The time complexity of this code is O(n^2), as both the transpose and reverse steps 
involve nested loops that iterate over all the elements in the matrix. 
The space complexity is O(1), as the rotation is performed in-place without allocating any additional data structures.
'''