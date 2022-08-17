from typing import Counter


def catiandupli(nums):

    hashMap=[]
    for i in nums:
        if i in hashMap:
            return True
        hashMap.append(i)
    return False

nums = [1,2,3,1]
print(catiandupli(nums))
print(Counter(nums))