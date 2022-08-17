from datetime import datetime # from tracemalloc import start
start = datetime.now()

l1 , l2 = [9,9,9,9,9,9,9],   [9,9,9,9]
tow1=[str(i) for i in l1[::-1]]
tow_str1=''.join(tow1)

tow2=[str(i) for i in l2[::-1]]
tow_str2=''.join(tow2)

SONG=(int(tow_str1)+int(tow_str2))
print(SONG)

we=[i for i in str(SONG)]
we=we[::-1]
we=[int(i) for i in we]
print(we)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start)[5:])