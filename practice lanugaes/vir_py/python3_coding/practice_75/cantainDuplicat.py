


def catDuplicat(nums):
    t=[]
    for n in nums:
        if n in t:  ## ye agar koi value in list me hai to true de de.
            return True    
        t.append(n)
    return False
nums = [1,2,3,1]
nums = [1,1,1,3,3,4,3,2,4,2]

# print(catDuplicat(nums))
# other methods is 
def cantDupSet(nums):
    return len(set(nums))!=len(nums)     # agar do no ki lumbi baraber  nahi  to true kar warna false kar

print(cantDupSet(nums))
print(set(nums))    # we allso use set

# getting all unique values inside the list
def uniquelist(nums):
    new=[]
    for n in nums:
        if n not in new:
            new.append(n)
        else:
            continue
    return new

print(
    uniquelist(nums)
)
