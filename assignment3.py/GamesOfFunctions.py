# write a python function to sum all the numbers in a list.

def sum(num):
    result = 0
    for i in num:
        result += i
    return result

list1 = [1,2,3,4,5]   
sum(list1)
print(sum(list1))
        