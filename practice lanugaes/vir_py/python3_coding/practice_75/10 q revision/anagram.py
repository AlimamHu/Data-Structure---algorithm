def anagram(s,t):
    if len(s)!=len(t):
        False

    Smap={}
    Tmap={}
    for i in range(len(s)):
        Smap[s[i]]=Smap.get(s[i],0)+1
        Tmap[t[i]]=Tmap.get(t[i],0)+1
    return Smap==Tmap



s = "anagram"
t = "nagaram"
print(anagram(s,t))