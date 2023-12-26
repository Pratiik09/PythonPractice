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


### Check Binary or Not ###
n = 1110

n_str = str(n)

for i in n_str:
    if i!='0' and i!='1':
        print("Not Binary")
        break
else:
    print("Is Binary")

### Swap Numbers w/o 3rd variable ###
a = 7
b = 2

a = a-b  # a=5
b = b+a  # b=7
a = b-a  # a=2

print(a,b)

# OUTPUT: 2,7

### Find Largest in List ###
input_list = [2,4,6,11,34,1,3]

def find_largest(inp_list):
  largest = inp_list[0]
  for elem in inp_list:
    if elem > largest:
      largest = elem
  return largest
  
print(find_largest(input_list))

### Bubble Sort ###
a = [3,1,4,2]

def bubblesort(arr):
  n = len(arr)
  for i in range(n-1):      # Iterate only n-1 times, because last element will be max right after 1st iteration (Optimization Perspective)
    for j in range(n-i-1):  # Everytime, we go 1 index less. If we don't add -1, it will give out og index error during 1st iteration
      if arr[j]>arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
    
  return arr
  
print(bubblesort(a))