from Week2_Ex2_data import * #import data from file - not recommended but done to create neater code
import time

atv = {'ucl.ac.uk':'ucl','google.co.uk':'google','wikipedia.org':'wiki'}    #this dictionary is used to map the user inputted web address to the variables. variables are shortened for ease of coding

fields = ['localip','webad','ip','ns','nsad','mxp','mailex','pns','rma','serial','timings'] #all data fields of a website relating to nslookup functions

NS = [0,1,3,4] #for each of these types, data fields are selected by indexing the fields array above
MX = [0,1,5,6]
SOA = [0,1,7,8,9,10]

method_list = [NS, MX, SOA] #combines field arrays for each method

nsmeth = {'NS':'0','MX':'1','SOA':'2'}   #dictionary containing each of the method lists to index positions in the method_list array


def print_record(): #define function for printing all records
    atvlist = list(atv.values())        #turn dictionary values into keys to be able to index
    print("Records available for:")
    for i in range(len(atvlist)):   #go through each element of the list
        print(dnsq[atvlist[i]]['webad'])    #use the atvlist values as the keys to access the main dictionary, and to print the data corresponding to the webad key in each sub-dictionary
    print("\n")



def nslookup(key):  #the key is the user input nslookup method
    print("nslookup using method:", key)    #provide visual feedback to user, especially when looking at different websites
    webname = input("Enter web address\n")  #prompts user
    if webname in atv.keys():   #checks if website is in the records

        key_sel = method_list[int(nsmeth[key])] #uses a dictionary to convert the method into indexes to access a list

        print("\nServer: ",localip,"\nAddress: ",localip,"\n\nNon-authoritative answer:")   #this is printed regardless of nslookup method
        for i in range(1,len(key_sel)): #checks number of features for the selected method, and loops that many times to print each of those features
            print(dnsq['defs'][fields[key_sel[i]]]) #prints text before the value eg. 'Mail Exchanger' = fdsjlkfdsj.com
            print(dnsq[atv[webname]][fields[key_sel[i]]],'\n')  #prints selected fields depending on which method is being used
        usein = input("Lookup another website (l)\nChange method (c)\nReturn to main menu (m)\n")    #prompt user
        if usein == 'l':    #if user wants to check another website with the same method, the function is restarted
            nslookup(key)   #the same nslookup method is passed to the function
        elif usein == 'c':  #to change the method, the user is sent to nslookupmenu, where they can change the method
            nslookup_menu()
        elif usein == 'm':  #if user wants to return to main menu, an exit status of 1 is returned, which skips through to the main function
            return 1
        elif usein == 'x':  #if user wants to exit during this sub menu, an exit status of 0 is returned, which is sent up to the main program
            return 0
        else:
            print("This is not a valid option, returning to menu\n")    #make sure the option is valid
            return 1
    elif webname == 'x':    #if user wants to exit while entering the website
        return 0    #exit status of 0 is returned
    else:
        print("This website is not on the records\n")   #if website record is not available, user is sent to start of function with the same key
        nslookup(key)




def nslookup_menu():
    while True: #runs endlessly as user may want to continue in this menu
        usein = input("Select lookup method (NS,MX,SOA)\n") #prompt user with options
        if usein == 'NS' or usein == 'MX' or usein == 'SOA':    #if the input is a valid method

            exit_status = nslookup(usein)   #assigns exit status if user wishes to exit from inside nslookup function #the user nslookup method is passed to this function
            if exit_status == 0:    #exit status is received and pushed to exit the main loop
                return 0
            elif exit_status == 1:  #if the exit status is 1, the program continues running and returns to menu
                return 1
            else:
                break
        elif usein == 'x':  #if the user wants to exit the program, an exit status of 0 is returned
            return 0
        else:   #if the option is not valid
            print("Enter a valid method\n")



while True: #program runs endlessly until it encounters a break
    process = input("What would you like to do?\n\t1.View record list (v)\n\t2.nslookup (n)\n\tExit any time by entering 'x'\n")    #promt user to select option
    if process == 'v':  #checks user input
        print_record()  #print record function defined above
    elif process == 'n':
        exit_status = nslookup_menu()   #nslookip menu defined above - presents further options for method selection
        if exit_status == 0:    #if x is entered while in the nslookupmenu function, the function returns 0 and the program exits
            break
    elif process == 'x':    #if user wants to exit
        break
    else:   #if the option is not valid, prompt user and return to menu
        print("Please enter valid option\n")
