### 43. Multiply Strings ###
"""
Input: num1 = "123", num2 = "456"
Output: "56088"
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        Example: 23 * 36
        n1 = 23
        n2 = 36
        This can be computed as
        = 6*3 + 6*20 + 30*3 + 30*20
        = 6*3 + 6*2*10 + 3*10*3 + 2*10*3*10
        As while multipying, we consider places (i.e. ones, tens)

        n2 in external loop - as one digit of n2 is multiplied with 
        each digit of n1 (in interanl loop)

        carry1 and carry2 is multiplied by 10 in each iteration for places
        """
        ans = 0
        carry2 = 1
        
        for n2 in num2[::-1]:
            carry1 = 1
            for n1 in num1[::-1]:
                ans += int(n2) * int(n1) * carry1 * carry2
                carry1 *= 10
            carry2 *= 10

        return str(ans)

