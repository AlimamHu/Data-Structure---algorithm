def cantainDuplicat(nums):
    hashmap=set()

    for i in nums:
        if i in hashmap:
            return True
        hashmap.add(i)
    return False

nums = [1,2,3]

print(cantainDuplicat(nums))