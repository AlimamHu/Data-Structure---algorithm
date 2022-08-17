def selfproduct(nums):
    res=[]
    for i in range(len(nums)):
        t=1
        if i+1 >=len(nums):
            break
        skipSelf=nums[:i-1] + nums[i+1:]
        print(skipSelf)
        # for n in :
        #     t*=n
        # res.append(t)
    # return res
nums = [1,2,3,4]
# selfproduct(nums)


def selfpro(nums):
    new_list=[]
    for i in range(len(nums)):
        # t=i
        self_t=1
        for ind , valu in enumerate(nums):
            if  ind==i:
                continue
            self_t*=valu
        new_list.append(self_t)

    return new_list

nums = [-1,1,0,-3,3]

print(selfpro(nums))