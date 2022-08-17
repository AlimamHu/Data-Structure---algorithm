

# input_list_values =input('enter you number: ')
# target=input("enter your target: ")

# def twoSum(nums:int, target: int):
#     return_list=[]
#     nums=[int(i) for i in input_list_values.split(",")] # convert into integer
#     target=int(target)

#     from_begning=list(range(len(nums)))   # start list from 0 to n. of list
#     e=list(range(1,len(nums)))  

#     row=iter(e)  # made list iterable

#     for I in from_begning:

#         try:
#             song =next(row)
#         except StopIteration:
#             break;

#         if (input_list_values[I]+input_list_values[song])==target: #9:  # target_values
#             return_list.append(I,song)

#     return return_list

# # print(twoSum(input_list_values,target))


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # self.val=nums
        # self.targ=target
        pass;

tow =Solution()
tow.twoSum([2,7,11,15],9)