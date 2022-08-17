# def function_x(x):
#     # x=55
#     t=[]
#     for i in range(1,x+1):

#         if x%i==0:
#             t.append(i)
#     return t
# # print(t)

# print(function_x(484))

primary_number_collection=[]
def function_x(x):
    global primary_number_collection
    t=[]
    for i in range(1,x+1):

        if x%i==0:
            t.append(i)
    
    if len(t)==2:
        return primary_number_collection.append(x)

# you can change easly those valriables
start_value=1    
end_value=200  # 400, 600, 1000

for i in range(start_value,end_value):
    (function_x(i))

print(primary_number_collection)

