

def slidingWindow1(nums,k):

    # if sliding window greater then lenght of list funtion return fulse
    if k>len(nums):
        return False
    # this slicing start from i position ent to k positions
    for i in range(len(nums)):
        print(
            sum(nums[i:k])
        )
        # i position seft +1 becouse for loop
        # k add 1 that help our window slide    
        k+=1
        # k after touching end position and higher then lenght of list , that give slicing error
        if k>len(nums):
            return False
    
nums= [100, 200, 300, 400]
nums = [1, 4, 2, 10, 2,3, 1, 0, 20]
k = 4
# slidingWindow1(nums,k)


# increase window size base from 0 to length of list
def sliceztoend(nums):
    # start position always 0
    k=0
    for i in range(len(nums)):
        # i position +1
        print(nums[k:i])
        
        # print(nums[k:i])
        # print(nums[k:i])
    
# sliceztoend(nums)s

# https://www.geeksforgeeks.org/window-sliding-technique/
# geekfromgeeks  
def maxsubsum(nums,k):
    # k window larger then nums that not working properly
    if k>len(nums):
        return False
    # max mum values come here
    max_values=0
    for i in range(len(nums)):
        # slicing start from i to k and k+=1
        # carrent values sum or last values sum which have max values 
        max_values=max(sum(nums[i:k]),max_values)

        k+=1
        # this goes last windows
        if k>len(nums):
            break
    return max_values
nums = [-1,-2,3,4]
k = 3

# print(maxsubsum(nums,k))


#   leetcode 2099
def subsquen(nums,k):
    new=[]
    for  i in range(len(nums)):
        new.append(nums[i:k])
        k+=1
        if k>len(nums):
            break
    sum_all_sub=[sum(i) for i in new]
    max_index=sum_all_sub.index(max(sum_all_sub))
    return new[max_index]
    # print(max_index,new)
     
# print(subsquen(nums,k))

def subsquence(s):
    # 0 to n-1
    for  i in range(len(s)):
        # 0 to i 
        for j in range(i):
            print(s[j:i],end=' ')
# subsquence('askdjflasjdfjs')
# subsquence('1234')

def subsquence(s):
    # 0 to n-1
    for  i in range(len(s)):
        # 0 to i 
        for j in range(i):
            print(s[j:i],end=' ')

nums = [2,1,3,3]
k = 2

# subsquence()
# from descuss pages
def maxSubsequence( nums, k):
    # sorted max k values get list  , then append to other empty list
    max_k,res=sorted(nums,reverse=True)[:k],[]
    for  i in nums:
    # each element from nums check in max k-th  True append empty list and remove from max_array
        if i in max_k:
            res.append(i)
            max_k.remove(i)
    # when length of max is 0 return empty list
            if len(max_k)==0:
                return res
nums = [-1,-2,3,4]
k = 3

# print(maxSubsequence(nums,k))


def subsquencelarg(nums,k):
    #get k length of list
    currwind=nums[:k]
    leng_num=len(nums)
    # after that list looops start to end of list
    for i in range(k,leng_num):
        # minimum values from curret window
        currmin=min(currwind)
        # checking current window start to end greater values

        if nums[i] > currmin:

            currwind.append(nums[i])
            # remvoe all smaller values and only adding greather values 
            currwind.remove(currmin)
    return currwind

print(subsquencelarg(nums,k))