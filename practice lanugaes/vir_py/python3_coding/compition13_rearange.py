# song=[1,2,3,4,5,6,7]   # [3,4,5,6,7, 1, 2]
# values=2

# for i in range(len(song)-values):
#     remove_values=song.pop()
#     song.insert(i,remove_values)
# print(song)


# for i in range(0,2):
#     song.append(song[i])
    # print(song.remove(song[i]))
    # song.append(song.remove(song[i]))
    # print(song.index(i))
import time
song=[6, 5, 3, 2, 8, 10, 9]
song.sort()

print(song)
song=[6, 5, 3, 2, 8, 10, 9]
print(set(song))

song=[6, 5, 3, 2, 8, 10, 9]
new=[]
for i in song:
    t=0
    if t<i:
        t+=i
        new.append(t)

print(new)