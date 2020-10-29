#for simplicity the ip addresses selected are ipv4 format

dnsq = {} #create empty dictionary

dnsq['ucl.ac.uk']='144.82.250.24'
dnsq['google.co.uk']='216.58.212.227'
dnsq['wikipedia.org']='91.198.174.192'  #populate dictionary with information


query = input("Do you want to query DNS or view all records?(q/v)\n")   #ask what user wants to do

if query == 'q':    ##if user wants to query DNS
    site = input("Enter web address\n") #user inputs web address they want to query
    if site in dnsq:    #check if the website exists in dictionary
        print("ip of selected site is", dnsq[site]) #print value accessed by key ie. return ip address for web address
    else:   #if the website is not in the dictionary
        print("This website does not exist in the records")
elif query == 'v':  #if user wants to view record
    ipq = input("Show associated ips? (y/n)\n") #ask if user wants to see web addresses only or the ip addresses of each
    if ipq == 'y':
        print(dnsq.items()) #returns web addresses and each of their ips
    elif ipq == 'n':
        print(dnsq.keys())  #returns web addresses only
