import time
start=time.time()
t=14
wort=int(t**0.5)



if t==wort**2:
    print(True)
else:
    print(False)
end=time.time()
print(round(end-start,10))