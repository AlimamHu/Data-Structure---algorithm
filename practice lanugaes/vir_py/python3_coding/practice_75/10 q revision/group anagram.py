from typing import DefaultDict


def groupana(strs):
    hashmap=DefaultDict(list)
    for s in strs:
        hashmap[str(sorted(s))].append(s)
    return hashmap.values()
strs = ["eat","tea","tan","ate","nat","bat"]

print(groupana(strs))