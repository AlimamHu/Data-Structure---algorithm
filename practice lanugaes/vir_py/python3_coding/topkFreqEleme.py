def topKfrq(nums,k):
    if len(nums)==1:
        return [1]
    hashK={}
    for n in nums:
        if n in hashK:
            hashK[n]+=1
        else:
            hashK[n]=1
    return list(decent(hashK).keys())[:k]
    
    
    # return sorted(hashK.values(),reverse=True)[:k]

def decent(hashK):
    return dict(sorted(hashK.items(), key = lambda x: x[1], reverse = True))

nums = [1,1,1,2,2,3]
k = 2

# nums = [1]
# k = 1

# print(topKfrq(nums,k))


# lleetcode here

def topKfreq(nums,k):
    count={}
    freq=[[] for i in range(len(nums)+1)]
    for n in nums:
        count[n]=1+count.get(n,0)
    for n , c in count.items():
        freq[c].append(n)
    res=[]
    for i in range(len(freq)-1,0,-1):
        for f in freq[i]:
            res.append(f)
            if len(res)==k:
                return res 
print(topKfreq(nums,k))