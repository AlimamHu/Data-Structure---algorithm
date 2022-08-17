

def bysort(s,t):
    return sorted(s)==sorted(t)
s = "anagram"
t = "nagaram"
# print(bysort(s,t))

def createhash(s):
    scant={}
    for  i in s:
        if i not in scant:
            scant[i]=1
        scant[i]+=1
    return scant


def hashmap(s):
    dic={}
    for i in s:
        dic[i]=1+dic.get(i,0)
    return dic
# print(hashmap(s))


def byhashmap(s,t):
    if len(s)!=len(t):
        return False
    scant,tcant=map(hashmap,[s,t])
    print(scant,tcant)
    return  scant==tcant
# print(byhashmap(s,t))


def neetcodehash(s,t):
    if len(s)!=len(t):
        return False
    hashs,hasht={},{}
    for i in range(len(s)):
        hashs[s[i]]=1+hashs.get(s[i],0)
        hasht[t[i]]=1+hasht.get(t[i],0)
    return hashs==hasht
print(neetcodehash(s,t))



