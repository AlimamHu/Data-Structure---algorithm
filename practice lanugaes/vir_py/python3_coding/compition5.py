# Palindrome Number
# t=10
# print(str(t) == str(t)[::-1])


class Solution:
    def reverse(self, x) :
        self.x=str(x)
        if self.x.startswith("-"):
            
            print(-int(self.x[::-1][:-1]))
        else:
            print( int(self.x[::-1]))
            
# 1534236469 -->  9646324351

song=Solution()
song.reverse(-823832123)

list1 = []
num = 6
 
while (num > 0):
    list1.append(num % 2)
    num = num//2
print(f"input values : {num} \nno of bits :{len(list1)}  {list1}")
for i in  reversed(list1):
    print(list1[i],end="")

print("\n",bin32(6)[2:])