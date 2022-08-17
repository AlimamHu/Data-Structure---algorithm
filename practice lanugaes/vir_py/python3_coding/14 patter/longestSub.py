def lonsub(s):
# substring all from string
    pre_leg=0
    index_leg=[]
    for i in range(len(s)):
        for t in range(i):
            # print(s[t:i])
            if len(s[t:i])>=len(s)-2:
# greater length values store
                pre_leg=len(s[t:i])
        
# # making list to greater value in list
                # index_leg.append([t,i])
                index_leg.append(s[t:i])
    return index_leg
s='aabbcc'
# print(lonsub(s))

def lengofsubKdis(s,k):
    new_dic={}
    current_window=0
    start_window,max_length=0,1
    for i in range(len(s)):
        cha=s[i]
        new_dic[cha]=i
        if len(new_dic.keys())>k:
            start_window=min(new_dic.values)
            print(new_dic.values.index(start_window) )
            # new_dic.
            start+=1
        current_window=i-start_window+1
        max_length=max(current_window,max_length)
    return max_length
lengofsubKdis(s,3)
