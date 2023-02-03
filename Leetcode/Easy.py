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

	inputNum = x
	newNum = 0
	while x>0:
		newNum = newNum * 10 + x%10
		x = x//10
	return newNum == inputNum

