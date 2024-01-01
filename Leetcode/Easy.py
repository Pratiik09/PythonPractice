### 9. Palindrome Number ###

""" 
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

# Approach 1: By converting to string
def isPalindrome(self, x: int) -> bool:
	if x < 0:
		return False
	
	return str(x) == str(x)[::-1]

# Approach 2: Without converting to string
def isPalindrome(self, x: int) -> bool:
	if x<0:
		return False

	input_num = x
	reveresed_num = 0
	while x>0:
		reveresed_num = reveresed_num * 10 + x%10
		x = x//10
	return reveresed_num == input_num


### 1. Two Sum ###

# Iterative Solution: O(n^2) as 2 nested for loops
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] ==  target:
                    res = [i,j]
                    return res

# Hashmap Approach: O(n) as 2 sequential loops
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

# Hashmap Approach: O(n) as only 1 for loop. Check complement and return index in 1 pass. Focus on add to dictionary part
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i


### 258. Add Digits ###
"""
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
"""

# For Loop + Recursion
class Solution:
    def addDigits(self, num: int) -> int:
        list_num = [int(i) for i in str(num)]
        sum_num = sum(list_num)
        if sum_num <= 9:
            return sum_num
        else:
            return self.addDigits(sum_num)


### 13. Roman to Integer ###
# Pseudo
"""
- Hashmap with values
- if small value before large one, subtract
- if large value before small, add

Eg.
Input: XIV
Output: 10 - 1 + 5 = 14
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {
            "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000
        }

        int_val = 0

        for i in range(len(s)):
            if i+1 < len(s) and roman_int[s[i]] < roman_int[s[i+1]]:
                int_val -= roman_int[s[i]]
            else:
                int_val += roman_int[s[i]]
        return int_val

