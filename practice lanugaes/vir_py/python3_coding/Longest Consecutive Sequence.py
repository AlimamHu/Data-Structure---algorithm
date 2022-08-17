def longconst(arr):
    res=0
    for i in arr:
        while i+1 in arr:
            res+=1
    return res
nums = [100,4,200,1,3,2]

# longconst(nums) 


def longconst(nums):
    nuset=set(nums)
    long=0
    for i in nuset:
        