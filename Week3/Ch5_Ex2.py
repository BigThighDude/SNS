
num = int(input("Enter integer to perform factorial operation:\n")) #prompt user to enter number, converts string to interger. program doesnt work if float is entered

def fact_iter(num):  #define iterative function
    product = 1  # define product before it is used
    for i in range(1,num+1):    #count up from 1 (works with 0 as the product is just returned as 0
        product = i*product #count up and multiply with each successive integer
    return product  #return the product to the main script

def fact_rec(num):
    if num==1:
        return 1
    else:
        return num*fact_rec(num-1)

# def fact_rec(num):  #define recursive function
#
#     product = product*fact_rec(num-1)   #function calls itself
#     return product  #function returns the final product ie. the factorial


if num>1:   #makes sure number is positive
    print("iterative ", fact_iter(num))    #run iterative program if input is valid
    print("recursive ", fact_rec(num))    #run recursive program if input is valid
elif num==1 or num==0:
    print("1")
else:   #if number is negative
    print("Enter valid number") #return error message
