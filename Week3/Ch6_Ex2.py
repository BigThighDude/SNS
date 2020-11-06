#Flow = set of packets with the same ip source, destination, tcp source port, tcp destination port
#for each flow, print ip source, ip destination, tcp port, bytes

import csv  #imports the csv module making it easier to handle csv files


with open('ws.csv') as csvfile: #use with open to ensure correct closing of file even with errors
    reader = csv.DictReader(csvfile, delimiter=',') #create a list called reader where each element is a dictionary
    newdict = {}    #create a new dictionary to turn list of dict into nested dict

    for item in reader:
        no = item.pop('No.')
        newdict[no] = item  #for loop to create the nested dictionary

    for i in range(0,len(newdict)): #for loop to remove any non TCP logs
        if newdict[str(i+1)]['Protocol'] != 'TCP':
            newdict.pop(str(i+1))
    keylist = list(newdict.keys())  #creates a list of keys corresponding to logs with TCP

    for i in range(0,len(keylist)): #this section of code extracts the tcp source and destination ports from the info section
        temp = newdict[str(keylist[i])]['Info'] #creates a temporary string from the info column
        temp = temp.split() #split string into list elements
        for j in range(0,len(temp)):    #this for loop checks if the element in the list is a number
            if temp[j].isdigit()==True: #if it is a number, it turns the string into an integer
                temp[j]=int(temp[j])
            else:   #if the element is not a number, it is replaced with zero
                temp[j]=0
        temp = [j for j in temp if j != 0]  #this deletes all zero elements of the temp list
        newdict[str(keylist[i])]['TCP_Source'] = temp[0]    #add new key to the newdict dictionaries to store info for the source tcp port
        newdict[str(keylist[i])]['TCP_Dest'] = temp[1]  #add new key to the newdict dictionaries to store info for the destination tcp port

    dict_data = {}  #create new dictioanry to store only the compared data - this reduces time and code complexity, but requires a few more steps
    for i in range(0,len(newdict)): #for each element of the tcp only dictionary
        dict_data[str(keylist[i])] = {} #create a nested dictionary for each element
        dict_data[str(keylist[i])]['Source'] = newdict[str(keylist[i])]['Source']
        dict_data[str(keylist[i])]['Destination'] = newdict[str(keylist[i])]['Destination']
        dict_data[str(keylist[i])]['TCP_Source'] = newdict[str(keylist[i])]['TCP_Source']
        dict_data[str(keylist[i])]['TCP_Dest'] = newdict[str(keylist[i])]['TCP_Dest']   #copy over data to be compared from the tcp reduced dictionary.


    dict_nodupe = {}  # create empty dictionary to populate with non duplicated flows
    for key, value in dict_data.items():    #this for loop goes through each element in the narrow dictionary and compares to the no dupe dictionary
        if value not in dict_nodupe.values():   #if this value does no exist in the nodupe dictionary, the value is written in
            dict_nodupe[key] = value

    ndkeys = list(dict_nodupe.keys())  #the keys from the nodupe dictionary are extracted into a list

    for i in range (0,len(ndkeys)): #print data from each of the fields required
        print("IP Source:", newdict[str(ndkeys[i])]['Source'], "IP Destination:", newdict[str(ndkeys[i])]['Destination'], "TCP Source:", newdict[str(ndkeys[i])]['TCP_Source'], "TCP Destination:", newdict[str(ndkeys[i])]['TCP_Dest'], "Bytes:", newdict[str(ndkeys[i])]['Length'])

    print("Total number of flows: ", len(ndkeys))   #print number of flows ie. unique ip/port combinations