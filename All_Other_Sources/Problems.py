### Transpose of Matrix using loops ###

matrix = [ [1,2,3], [4,5,6] ]

transposed_matrix = []

for i in range( len(matrix[1]) ):
    transpose_stage = []
    
    for row in matrix:
        print(row[i])
        transpose_stage.append(row[i])
    transposed_matrix.append(transpose_stage)
    
print(transposed_matrix)

# OUTPUT:
[[1, 4], [2, 5], [3, 6]]


### Transpose of Matrix using List Comprehension ###

matrix = [ [1,2,3], [4,5,6] ]
transpose = [ [ row[i] for row in matrix ] for i in range(len(matrix[0])) ]
print(transpose)

# OUTPUT:
[[1, 4], [2, 5], [3, 6]]