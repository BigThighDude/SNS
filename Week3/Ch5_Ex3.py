import random

a = []

for i in range(0,5):
    a = a +[random.randint(0,10)]

def list_order(mylist):
    mylist.sort()
    return mylist


print(list_order(a))