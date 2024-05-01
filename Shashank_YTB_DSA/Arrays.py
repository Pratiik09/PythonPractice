### 1. Two Sum Problem - In Leetcode Easy ###

### 2. Majority Element ###
"""
Find the majority element in the array. A majority element in an array A[] of size n is an element that appears more than n/2 times 
(and hence there is at most one such element). 

Examples : 

Input : A[]={3, 3, 4, 2, 4, 4, 2, 4, 4}
Output : 4
Explanation: The frequency of 4 is 5 which is greater than the half of the size of the array size. 

Input : A[] = {3, 3, 4, 2, 4, 4, 2, 4}
Output : No Majority Element
Explanation: There is no element whose frequency is greater than the half of the size of the array size.
"""

# Hashmap Solution with Sorting - My First Attempt
# Time Complexity: O(n logn)
# As sorting in Python = O(nlogn) and loop takes O(n)

a = [3, 3, 4, 2, 4, 4, 2, 4, 4]
freq = {}

for e in a:
  if e in freq:
    freq[e] += 1
  else:
    freq[e] = 1

sorted_dict = sorted( freq.items(), key = lambda x: x[1], reverse = True)

if sorted_dict[0][1] >= len(a)/2:
  print("Majority Element:", sorted_dict[0][0])
else:
  print("No Majority Element")


# Hashmap Solution without Sorting
# TC = O(n) As only 1 Loop is present
a = [3, 3, 4, 2, 4, 4, 2, 4, 4]
freq = {}

majority_elem = 0    # Dummy

for e in a:
  if e in freq:
    freq[e] += 1
    if freq[e] > len(a)/2:
      majority_elem = e
      break
  else:
    freq[e] = 1

if majority_elem:
  print("Majority Element:", majority_elem)
else:
  print("No Majority Element")


### 3. Find the Number Occurring Odd Number of Times
"""
Given an array of positive integers. All numbers occur an even number of times except one number which occurs an odd number of times. Find the number in O(n) time & constant space.

Examples : 

Input : arr = {1, 2, 3, 2, 3, 1, 3}
Output : 3

Input : arr = {5, 7, 2, 7, 5, 2, 5}
Output : 5
"""

# Using Hashmaps - My Approach
# TC = O(n) - As no nested loops

a = [1, 2, 3, 2, 3, 1, 3, 1, 3]
freq = {}

odd_flag = 0

for e in a:
  if e in freq:
    freq[e] += 1
  else:
    freq[e] = 1

for k,v in freq.items():
  if v%2==1:
    odd_flag = 1
    print(f"Odd occuring number is {k}")

if not odd_flag:
  print("No Odd occuring number")


### 4. Merge an array of size n into another array of size m+n - In Leetcode Easy 88. Merge Sorted Array ###

