#!/usr/bin/python3
"""
Pascal triangle
"""

def pascal_triangle(n):
    """Function to give pascal's triangle with n rows"""
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
    
        for j in range (1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)
    return (triangle)