#1
def CountDown(n):
    return list(range(n,-1,-1))
#2
def printandreturn(lst):
    print (lst[0])
    return lst[1]

#3 
def first_plus_length(lst):
    return lst[0] + len(lst)
#4

def Values_Greterthan_second(lst):
    if len(lst)<2:
        return False 
    second_item=lst[1]
    new_list=[]

    for x in range(len(lst)):
        if lst[x]>second_item:
            new_list.append(lst[x])
    
    print(len(new_list))
    return new_list

print(Values_Greterthan_second([5,2,3,2,1,4]))

#5
def This_length_That_Value(lenght,value):
    new_list=[]
    for x in range(lenght):
        new_list.append(value)
    return new_list

print(This_length_That_Value(4,7))
print(This_length_That_Value(6,2))