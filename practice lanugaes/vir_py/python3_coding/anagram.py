

# s = "rat"
# t = "car"

# s="a"
# t="ab"
def anagramfuncation(s,t):

    if len(s)!=len(t):
        return False

    first=[]
    first.extend(s)
    ans=[]
    for i in first:
        if i in t:
            ans.append(True)
        else:
            ans.append(False)
    return all(ans)



# print(anagramfuncation(s,t))
def hashmap(s):
    s2={}
    # t2={}
    for i in s:
        if i in s2:
            s2[i]=s2[i]+1
        else:
            s2[i]=1
    return s2

def anagramFunv2(s,t):
    
    hashS, hashT= list(map(hashmap,[s,t]))
    print(hashS)
    print(hashT)

    return hashS==hashT
s = "anagram"
t = "nagaram"

s="anagram"
t="nagaram"

# s = "rat"
# t = "car"
# print(anagramFunv2(s,t))


#    by neetcode help

def isAnagram(s,t):
    # return sorted(s)==sorted(t)         we can also use them 
    if len(s)!=len(t):
        return False
    hashS, hashT,={},{}
    for i in range(len(s)):
        hashS[s[i]]=1+hashS.get(s[i],0)
        # print(hashS)
        hashT[t[i]]=1+hashT.get(t[i],0)
    print(hashS,hashT)
    return hashS==hashT
print(isAnagram(s,t))