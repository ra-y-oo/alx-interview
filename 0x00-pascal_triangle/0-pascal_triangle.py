def pascal_triangle(n):
    if n <= 0:
        return []
    
    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]
    
    for i in range(1, n):
        # Generate the next row based on the previous row
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        
        triangle.append(new_row)
    
    return triangle

# Example usage:
n = 5
result = pascal_triangle(n)
for row in result:
    print(row)
