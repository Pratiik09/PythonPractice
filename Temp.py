  def addBinary(self, a: str, b: str) -> str:
    res = ""
    carry = 0

    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        digitA = int(a[i]) if i >= 0 else 0
        digitB = int(b[j]) if i >= 0 else 0

        total = digitA + digitB + carry
        digitR = total % 2
        res += str(digitR)
        carry = total // 2
    
        i -= 1
        j -= 1

    return res