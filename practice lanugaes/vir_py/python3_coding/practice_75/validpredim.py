

def validpre(s):
    # s=s.replace([' ','/',"'",",",'"'],"")
    # print(s)
    new_s=''
    for i in s:
        if i.isalnum():
            new_s+=i
    new_s=new_s.lower()
    return new_s==new_s[::-1]
s = "race a car"
s = " "
s = "A man, a plan, a canal: Panama"
# print(validpre(s))


def is_alpha(s):
    A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a=A.lower()
    n=[0,1,2,3,4,5,6,7,8,9]
    if s in A:
        print('THIS IS ALPHA')
        return True

    print('this not alph')
    return False
# print(is_alpha('a'))


# by neetcode help
def validpre(s):
    l,r=0,len(s)-1
    while r>l:
        while r>l and not s[l].isalpha():
            l+=1
        while r>l and not s[r].isalpha():
            r-=1
        if s[r].lower()!=s[l].lower():
            return False
        l+=1
        r-=1
    return True
s='0P'
print(validpre(s))
