def recursive(nums,target):
    low,high=0,len(nums)-1

    while low<=high:
        mid=high-low
        if target not in nums:
            return f'not having this values'
        if target==nums[mid]:
            return mid
        else:
            if target<nums[mid]:
                high=mid
            else:
                low=mid
        low+=1
        high-=1




nums=[1,2,3,4,5,6,7]
target=1

print(recursive(nums,target))
