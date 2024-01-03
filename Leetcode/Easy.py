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
Till output is a single digit number
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

### 66. Plus One ###
"""
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""
# Pseudo
"""
- if digit is 9, make digit 0 and carry 1 while loop keeping carry = 0 as exit condition
"""

# (Left to Right) Reverse Traversal
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]

        carry = 1
        i = 0

        while carry==1:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            i += 1
        return digits[::-1]

# Right to Left Trasversl
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits)-1

        while carry==1:
            if i < len(digits):
                if i==-1:
                    digits.insert(0, 1) # (index, object)
                    digits[i+2] = 0
                    carry = 0
                elif digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.insert(0, 1) # (index, object)
                carry = 0
            i -= 1
        return digits

### 67. Add Binary ###
"""
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
#  Reverse Way (Left to Right)
class Solution:
  def addBinary(self, a: str, b: str) -> str:
    res = ""
    carry = 0
    a = a[::-1]
    b = b[::-1]

    for i in range(max(len(a), len(b))):
        digitA = int(a[i]) if i < len(a) else 0
        digitB = int(b[i]) if i < len(b) else 0

        total = digitA + digitB + carry
        digitR = total % 2
        res += str(digitR)
        carry = total // 2
    
    if carry==1:
        res += str(carry)
    
    return res[::-1]

# Right to Left
class Solution:
  def addBinary(self, a: str, b: str) -> str:
    res = ""
    carry = 0

    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        digitA = int(a[i]) if i >= 0 else 0
        digitB = int(b[j]) if j >= 0 else 0

        total = digitA + digitB + carry
        digitR = total % 2
        res = str(digitR) + res
        carry = total // 2
    
        i -= 1
        j -= 1

    return res


### 415. Add Strings ###
"""
Same question as above, only for decimal. Only changed div and mod to 10

Example - Add 2 deciaml numbers
Input: num1 = "456", num2 = "77"
Output: "533"
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        carry = 0

        i = len(num1)-1
        j = len(num2)-1

        while i>=0 or j>=0 or carry:
            digit1 = int(num1[i]) if i>=0 else 0
            digit2 = int(num2[j]) if j>=0 else 0

            total = carry + digit1 + digit2
            digitR = total % 10
            res = str(digitR) + res
            carry = total // 10

            i -= 1
            j -= 1

        return res

### 989. Add to Array-Form of Integer ###
"""
Same question as above, only Input is in Array form

Example:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
"""
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num1 = "".join([str(x) for x in num])
        num2 = str(k)
        
        res = ""
        carry = 0

        i = len(num1)-1
        j = len(num2)-1

        while i>=0 or j>=0 or carry:
            digit1 = int(num1[i]) if i>=0 else 0
            digit2 = int(num2[j]) if j>=0 else 0

            total = carry + digit1 + digit2
            digitR = total % 10
            res = str(digitR) + res
            carry = total // 10

            i -= 1
            j -= 1

        result = [int(x) for x in res]

        return result

### 14. Longest Common Prefix ###
"""
Input: strs = ["flower","flow","flight"]
Output: "fl"

If no match, return ""
"""
# My Solution - Iterated through all Strings
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        temp = []
        len_strs = len(strs)
        min_len_str = min(strs, key=len)
        len_min_str = len(min_len_str)

        flag = 1

        for i in range(len_min_str):
            temp.append(min_len_str[i])
            for j in range(len_strs):
                if strs[j][i] == temp[0]:
                    if j == len_strs - 1 and flag==1: # Break to handle last string of strs list
                        common += temp[0]
                        break
                else:
                    flag = 0
                    break
            
            temp.pop()

        return str(common)

"""
Sort and Check only for 1st and last strings in List
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        strs = sorted(strs)
        first_str = strs[0]
        last_str = strs[-1]

        for i in range( min(len(first_str), len(last_str))):
            if first_str[i]==last_str[i]:
                common += first_str[i]
            else:
                return str(common)
        return str(common)
            
### 20. Valid Parentheses ###
"""
Check for Valid Parenthesis, Input string consists of only these
'(', ')', '{', '}', '[' and ']'

Example:
Input: s = "()[]{}"
Output: true
"""

"""
1. Use close_to_open Hashmap, rest is simple
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for c in s:
            if c in close_to_open:
                if stack and stack[-1]==close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

### 26. Remove Duplicates from Sorted Array ###
"""
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

"""
My Solution:
Not in-place, it needs extra space for storing uniques list.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniques = []
        for e in nums:
            if e not in uniques:
                uniques.append(e)
        k = len(uniques)
        for i in range(k):
            nums[i] = uniques[i]
        return k

"""
Two Pointer in-place approach
O(1) space complexity
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        l = left pointer
        r = right pointer
        """
        l = 1 # Because 1st element i.e. Index 0 is always 1st and Unique occurance
        # Also, r will also start from 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l