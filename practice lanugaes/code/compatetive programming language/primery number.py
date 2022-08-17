# finding range of reminder
def function_pri(x):  

    reminder_x=[]
    for i in range(1,x+1):
        reminder_x.append(x%i==0)
    par_unit=len(reminder_x)
    if par_unit==2:
        print(f"this is primary no. {x}")
        return x
    else:
        print(f'opps this is not primary number  {x}')
    # return reminder_x


# for i in range(1,200):
#     function_pri(i)
# # 
function_pri(53)

def len_counter():
    unit_value=function_pri(33)
    if len(unit_value)==2:
        print(f"this is primary no. {unit_value[-1]}")
    else:
        print(f'opps this is not primary number  {unit_value[-1]}')
    # print(len(unit_value))
# len_counter()