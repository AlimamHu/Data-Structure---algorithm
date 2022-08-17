#Add Binary
class Solution:
    def addBinary(self, a, b):
        self.a=a
        self.b=b
        return bin(int(self.a,2)+int(self.b,2))[2:]

class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            sum = carry;
            if i >= 0 : sum += ord(a[i]) - ord('0') # ord is use to get value of ASCII character
            if j >= 0 : sum += ord(b[j]) - ord('0')
            i, j = i - 1, j - 1
            carry = 1 if sum > 1 else 0;
            res += str(sum % 2)

        if carry != 0 : res += str(carry);
        return res[::-1]
import time
nrw=Solution1()

print(nrw.addBinary("11","1"))


nrw_now_start=time.time()
older=Solution()

print(older.addBinary("11","1"))


nrw_end=time.time()

print("first class function values : ",nrw_end-nrw_now_start)
