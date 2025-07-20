#1
def biggie_size(lst):
    for x in range(len(lst)):
        if lst[x]>0:
            lst[x]="big"
    return lst

print(biggie_size([-1,3,5,-5]))

#2
def count_positives(lst):
    positiv_num = 0
    for x in range(len(lst)):
        if lst[x] >0:
            positiv_num += 1
    lst[-1] =positiv_num
    return lst
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

#3
def sum_total(lst):
    sum = 0
    for x in range(len(lst)):
        sum += lst[x]
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

#4
def average(lst):
    sum =0
    avg =0
    count =0
    for x in range(len(lst)):
        sum += lst[x]
        count += 1
    avg=sum/count
    return avg
print(average([1,2,3,4]))

#5
def length(lst):
    leng = 0
    for x in range(len(lst)):
        leng +=1
    return leng
print(length([37,2,1,-9]))

#6
def minimum(lst):
    if len(lst)== 0:
        return False
    mini = lst[0]
    for x in range( 1,len(lst)):
        if mini > lst[x] :
            mini=lst[x]
    return mini
print(minimum([37,2,1,-9]))
print(minimum([]))

#7
def maximum(lst):
    if len(lst) == 0 :
        return False
    maxi = lst[0]
    for x in range(len(lst)):
        if lst[x]> maxi:
            maxi=lst[x]
    return maxi
print(maximum([37,2,1,-9]))
print(maximum([]))

#8
def ultimate_analysis(lst):
    my_dict={"sum Total":sum_total(lst),"average":average(lst),"minimum":minimum(lst),"maximum":maximum(lst)}
    return my_dict
print(ultimate_analysis([37,2,1,-9]))

#9 
def reverse_list(lst):
    start =0
    end=len(lst) - 1
    for x in range(len(lst)):
        if start >= end:
           break
        temp = lst[start]
        lst[start] = lst[end]
        lst[end]=temp
        sta````````````````````````````````````````rt += 1
        end -= 1
    return lst

print(reverse_list([37,2,1,-9])) 