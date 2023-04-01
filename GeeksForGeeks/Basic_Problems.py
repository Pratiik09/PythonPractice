### Maximum of 2 Numbers ###

# Approaches:
# if-else | max() function | Ternary operator | Lambda function | List Comprehension | sort() and fetch list[-1]


### Factorial Problem ###

# Approach: Recursion

n = 5

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
val = factorial(n)
print(val)

OUTPUT: 120

# Approach Iterative using for loop

# Approach numpy.prod()

import numpy as np

n = 5

fact = np.prod( [i for i in range(1, n+1)] )
print(fact)


### Simple Interest ###

# Formula = (P * T * R) / 100
# Where P = Principle Amount, T = Tenure, R = Rate of Interest
# Appproach = Simple Multiplication


### Compound Interest ###

# Formula:
# A = P(1 + R/100) ^ t 

# Compound Interest = A – P 

# Where, 
# A is amount 
# P is the principal amount 
# R is the rate and 
# T is the time span

# Approach: Use either pow(x,y) function or x**y to compute the power value


### Armstrong Number in O(n) ###

# 153 is Amrstrong Num if 1*1*1 + 5*5*5 + 3*3*3 = 153

num = 153
str_num = str(num)
sum_w_order = 0

order = int(len(str(num)))

for i in str_num:
    sum_w_order += pow(int(i), order)
    
if num == sum_w_order:
    print(True)
else:
    print(False)

OUTPUT: True

# Approach to get answer in O(logn)

num = 153
str_num = str(num)
sum_w_order = 0

order = int(len(str(num)))

while num != 0:
    rem = num % 10  # Extract last digit of the number
    sum_w_order += pow(rem, order)  # Finding last_digit ** order
    num = num // 10  # Getting the number remaining after extracting last digit after floor division
    
if int(str_num) == sum_w_order:
    print(True)
else:
    print(False)


### Print Prime numbers in a range ###
start = 2
end = 7
prime_list = []

def CheckPrime(s, e):
    for num in range(s, e+1):
        if num <= 1:
            continue
        else:
            for den in range(2, (num//2)+1):
                if num % den == 0:
                    break
            else:
                prime_list.append(num)
    return prime_list
    
print( CheckPrime(start, end) )

OUTPUT: [2, 3, 5, 7]

### Check Prime ###
num = 6

def CheckPrime(n):
    if n <= 1:
        return False
    else:
        for den in range(2, (n//2)+1):
            if n % den == 0:
                return False
        else:
            return True

print(CheckPrime(num))

OUTPUT: False

# Approach: Instead of checking for ( 2, int(n/2) ) , we can check for ( 2, sqrt(n)+1 )

### Find nth Fibonacci Number ###
def Fibonacci(n):
    if (n <= 0):
        print("Incorrect Input")
    elif n == 1:  # Base case 1
        return 0
    elif n == 2:  # Base case 2
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
        
print( Fibonacci(7) )

OUTPUT: 8

# Time Complexity: O(2^N)


# In any recursion problem, base case is important to get an exit. Here n==1 and n==2 are base cases

# Fibonacci Series: 0, 1, 1, 2, 3, 5, 8

# The time complexity of this program is O(2^n) because for each call to the Fibonacci function, 
# two more calls are made, leading to an exponential growth of the number of function calls

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

## Dynamic Approach as we are solving the problem from a bottom-up method (as we are calculating from 1st number to nth number) to solve the problem
def Fibonacci(n):
    a = 0
    b = 1
    
    if n < 0:
        print("Wrong Input")
    elif n == 0:
        return a  ## For base case
    elif n == 1:
        return b  ## For base case
    else:
        for num in range( 2, n ):
            c = a + b  ## Getting the next number in the series
            a = b
            b = c
        return b       ## Returning the current value of b
    
print( Fibonacci(7) )

# Time Complexity: O(N)


### Sum of square of 1st n natural numbers ###
n = int( input("Enter Count: ") )

list_num = [i for i in range(1, n+1)]

sum = 0

for num in list_num:
    sum += (num**2)
    
print(sum)

INPUT: 10
OUTPUT: 55 
# Time Complexity: O(n) as 2 loops are running but each take O(n), which would be O(n) + O(n) = O(2n) = O(n)

# Approach: Formula: sum = ( n * ( n+1 ) * ( 2*n+1 ) ) / 6
# Time Complexity: O(1)


### For Sum of Cube of 1st n natural numbers ###
# Approach: Formula: sum = (n ( n + 1 ) / 2) ^ 2 
# Time Complexity: O(1)

