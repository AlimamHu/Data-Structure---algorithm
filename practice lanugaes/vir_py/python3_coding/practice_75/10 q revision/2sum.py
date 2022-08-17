def Twosum(nums,target):
    # makes hashmap
    hashmap={}
    # make differnce target to each index
    for i in range(len(nums)):
        # make difference values 
        diff=target-nums[i]
        
    # if get difference in hashmap
        if diff in hashmap:
            return [hashmap[diff],i]
    # add differnce to i in hashmap
        hashmap[nums[i]]=i
    # return postion i position & hashmap[diff] values
    
nums = [2,7,11,15]
target = 9
print(Twosum(nums,target))