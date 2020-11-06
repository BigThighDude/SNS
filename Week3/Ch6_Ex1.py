import csv  #imports the csv module making it easier to handle csv files


with open('ws.csv') as csvfile: #use with open to ensure correct closing of file even with errors
    reader = csv.DictReader(csvfile, delimiter=',') #create a list called reader where each element is a dictionary
    record = input("Enter record number to view using a space to separate each field\n")  # which row user wants to see
    record = record.split()  # split column fields into separate elements in the attributes list
    attribute = input("Enter data fields to view using a space to separate each field\n")    #which column user wants to see
    attribute = attribute.split()   #split column fields into separate elements in the attributes list
    for row in reader:  #iterate through dictreader object
        for j in range(0,len(record)):  #in case user requests multiple records, iterate through all the requested records
            if row['No.']==record[j]:  #only continue if the user requested the specific record
                for i in range(0,len(attribute)):
                    print("Record no: ", record[j-1], str(attribute[i]), row[attribute[i]])    #iterate through each attribute requested

