digits = [4,3,2,1]
t=""

for i in digits:
    t+=str(i)

new_=[]
for i in str(int(t)+1):
    new_.append(int(i))
print(new_)

print(("".join([str(i) for i in digits])))
# song=str(int("".join([str(i) for i in digits]))+1)
# print([int(x) for x in    ])
print([int(i) for  i in  str(int("".join([str(i) for i in digits]))+1)  ])