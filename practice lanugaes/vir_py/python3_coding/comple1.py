
    
def twosum(input_list_values,target):
   
    from_begning=list(range(len(input_list_values)))   # start list from 0 to n. of list
    e=list(range(1,len(input_list_values)))             # start list from 1 to no. of list
    

    row=iter(e)  # made list iterable

    for I in from_begning:

        try:
            song =next(row)
        except StopIteration:
            break;

        if (input_list_values[I]+input_list_values[song])==target: #9:  # target_values
            return [I,song]

print(twosum([2,7,11,15],9))


