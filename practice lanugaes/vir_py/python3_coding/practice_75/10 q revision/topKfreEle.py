# not done

def topkelimemnt(nums,k):
    hashmap={}

    for i in range(len(nums)):
        hashmap[nums[i]]=1+hashmap.get(nums[i],0)
    hash_values=sorted(list(hashmap.values()),reverse=True)

    print(hashmap.get((hash_values[:k])))
nums = [1,1,1,2,2,3]
k = 2
topkelimemnt(nums,k)