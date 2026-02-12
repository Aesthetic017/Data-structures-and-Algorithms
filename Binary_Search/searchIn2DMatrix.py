'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Input: matrix = [[1,4,7,11,15],
                [2,5,8,12,19],
                [3,6,9,16,22],
                [10,13,14,17,24],
                [18,21,23,26,30]] 
                
target = 5

Output: true 
'''

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    total_rows = len(matrix)
    total_cols = len(matrix[0])

    row = 0
    col = total_cols - 1   # start at top-right

    while row < total_rows and col >= 0:
        current = matrix[row][col]

        if current == target:
            return True
        elif current < target:
            row += 1     # move down
        else:
            col -= 1     # move left

    return False


matrix = [
    [1,  4,  7,  11, 15],
    [2,  5,  8,  12, 19],
    [3,  6,  9,  16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

print(searchMatrix(matrix, 14))  
      
            
        