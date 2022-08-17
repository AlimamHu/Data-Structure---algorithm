

nums = [-1,1,0,-3,3]

def prodsection(l):
    eachInsideList=1
    for  i in l:
            eachInsideList=i*eachInsideList
    return eachInsideList
lestnew=[1,2,4,5]
# print(prodsection(lestnew))

def selfproduct(nums):
    prod=[]
    for i in range(len(nums)):
        for t in range(len(nums)):
            prod.append(nums[i:t])
            print(i,t)
    print(prod)
    result=[]
    for eachlist in prod:
        # print(list(map(prodsection,eachlist)))
        mulitiy=prodsection(eachlist)
        result.append(mulitiy)
        # print(eachlist)
    # for i in prod:
        # pass
    print(result)
    return max(result)
nums = [2,3,-2,4]
nums = [-2,0,-1]

# print(selfproduct(nums))

# above code is miss understanding the question & by misstake solve other question

def expectself(nums):
    tweet=[]
    for  i,v  in enumerate(nums):
        temp=nums.copy()
        temp.remove(v)
        product_come=prodsection(temp)
        tweet.append(product_come)
    


    return tweet
nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]

# print(expectself(nums))


# O(n)
def oselfProd(nums):
    pre=1
    post=1
    prefi=[]
    postfix=[]
    for i,v in enumerate(nums):
        # print(3-i)
        pre=pre*v
        prefi.append(pre)

        post=post*nums[(len(nums)-1)-i]
        postfix.append(post)

    print(prefi)
    print(postfix)
    # pass
# oselfProd(nums)

# neetcode solution here 

def selfpro(nums):
    res =[1]*len(nums)

    prefix=1
    for i in range(len(nums)):
        res[i]=prefix
        prefix*=nums[i]
    prefix=1
    for i in range(len(nums)-1,-1,-1):
        res[i]*=prefix
        prefix*=nums[i]
    return res
    pass
selfpro(nums)