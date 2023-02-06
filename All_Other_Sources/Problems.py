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

### Reverse Integer without converting to String ###

n = 1234
r = 0

while n > 0:
    r = r*10 + n%10
    n = n//10
print(r)


### Print Fibonacci Series using Iterative Approach ###
a, b = 0, 1

n = 7  # Number of Fibonacci Elements

fib_list = []

for i in range(0, n):
    if i <= 1:
        c = i
    else:
        c = a + b
        a = b
        b = c
    fib_list.append(c)
    
print(fib_list)

### Print Fibonacci Series using Recursive Approach ###
num = 7  # Number of Fibonacci Elements

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
       
fib_list = []

for i in range(0,num):
    fib_list.append( fibonacci(i) )

print(fib_list)


###  ###