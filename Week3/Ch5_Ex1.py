import random   #used to create the list

a=[]    #create empty list to concatenate randomly generated integers to

for i in range(0,5):    #repeat for as many elements as you want in list a
    a = a+[random.randint(0,10)]    #concatenate randomly generated number to the list a

print(a)    #show the created list

def max_val(list):  #create function to which the list is passed
    list.sort() #use built-in function sort in ascending order
    return a[-1]    #largest value is final element in list

print(max_val(a))   #run the function by passing a to it, and print the answer

print(len(a))