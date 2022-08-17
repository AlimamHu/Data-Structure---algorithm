from collections import defaultdict
# from itertools import count
# from numpy import sort


def groupAnagram(strs):
    # hashStrs={}
    # for i,v in enumerate(strs):
    #     sortedVluse=''.join(sorted(v))

    #     if sortedVluse in hashStrs:
    #         strs[i]=sortedVluse
    #         hashStrs[sortedVluse]=hashStrs[sortedVluse]+1
    #     else:
    #         hashStrs[sortedVluse]=1
    #     # strs[i]=(''.join(sorted(v)))
    # newStrs=[]
    # for i in hashStrs:
    #     hashStrs

    # print(hashStrs,strs)
    # for i in strs:
        # strs[i]=''.join(sorted(i))
    for i,v in enumerate(strs):
        
        strs[i]=''.join(sorted(v))
    print(sorted(strs))



strs = ["eat","tea","tan","ate","nat","bat",'toon']
# groupAnagram(strs)

#  by neetcode 

def groupAna(strs):
    res=defaultdict(list)
    for s in strs:
        count=[0]*26  # a----z 
        for c in s:
            count[ord(c)-ord('a')]+=1  # count[3]=++1   ; e=3
        res[tuple(count)].append(s)   #res[3,0,0,....1]='eat'
    print(res.values())
    # print(count)
groupAna(strs)