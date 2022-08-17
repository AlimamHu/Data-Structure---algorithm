l=[12,345,2,6,7896]
l=[str(i) for i in l]
t=0
for i in l:
    
    
    if len(i)%2==0:
        t+=1
print(t)