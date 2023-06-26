# write a python function that accepts a string and 
# calculate the number of upper case letters and lower case letters.

def  string(s):
    lower = 0
    upper= 0
    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        else:
            pass
    return(upper,lower)       
string1 = "Edyoda  Python Assignment"
print(string(string1))            

