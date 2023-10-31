def sum_boundary_elements(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    boundary_sum = 0
    
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                boundary_sum += matrix[i][j]
    
    return boundary_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = sum_boundary_elements(matrix)
print(f"The sum of boundary elements is: {result}")
