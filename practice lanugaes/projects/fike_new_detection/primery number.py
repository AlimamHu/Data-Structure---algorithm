print('HELLO ALIMAM')
print(4%1==0)
print(4%4)
t=[]
for i in range(1,10):
    if i%1==0 :  #and i%1==0
        t.append(i)
    
print(t)

def check_code(x):
    print(x%1==0)
    print(x%x==0)
check_code(34)