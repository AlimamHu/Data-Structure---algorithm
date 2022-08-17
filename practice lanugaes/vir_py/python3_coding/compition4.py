# Duplicate Zeros
arr = [1,0,2,3,0,4,5,0]  #--->  [1,0,0,2,3,0,0,4]
arr2 = [1,0,2,3,0,4,5,0]
arr3 = [str(i) for i in arr]
for index, values in enumerate(arr3):
    if values=="0":
        # arr2.insert(index,0)
        print(values*2)
        print(index,0)

    
# print(arr2)