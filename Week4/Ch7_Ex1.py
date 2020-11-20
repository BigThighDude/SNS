

n = 6
data=[[0 for column in range(n)] for row in range(n)]   # initialise list of size nxn (number of nodes) with zeros

long_matrix = '025100203200530315123010001102005020'    # write down connectivity matrix in long form - easier to enter data. zero represents self or infinity


lmi = 0 # counter to interate through long matrix
for i in range(n):  # loop to enter connectivity matrix from long form into nested list
    for j in range(n):
        data[i][j]=int(long_matrix[lmi])
        lmi+=1


nodelist = ['A','B','C','D','E','F']    # generate list containing name of nodes

class network:  # defining what a node is

    def __init__(self, data, nodelist, sn, en):    # initialise network with data given
        self.data = data
        self.nodelist = nodelist
        self.sn = sn
        self.en = en

    def dist_meas(self):
        temp = data # dont want to change the original data

        si = nodelist.index(sn) # starting node index
        ei = nodelist.index(en) # ending node index

        lenlist = [[0]*len(nodelist)]*4 # 4 rows - first is the distance, second is predecessor, third is termination status, fourth is for additional space to simplify code

        lenlist[0] = temp[nodelist.index(sn)]   # initialising first row from user selected node - using data
        lenlist[1] = [nodelist[nodelist.index(sn)]]*len(nodelist) # second row - predecessor initialised with first starting node value
        lenlist[2] = [0] * len(nodelist) # third row termination status - all set to zero
        lenlist[2][si] = 1  # starting node status set to 1
        lenlist[3] = [0] * len(nodelist)  # fourth row working space - all set to zero

        node = si   # for the initial value

        while lenlist[2][ei] != 1:
            for i in range(len(nodelist)):
                if temp[i][node] < lenlist[0][i] and lenlist[2][i] == 0:
                    lenlist[0][i] = temp[node][i]
                    lenlist[1][i] = nodelist[node]
                if lenlist[2][i] != 1:
                    lenlist[3][i]=lenlist[0][i]

                temp[i][node] = 0
                temp[node][i] = 0

            node = lenlist[3].index(min(i for i in lenlist[3] if i != 0))
            lenlist[2][node] = 1
        return lenlist, temp







print("System nodes are: ", nodelist)    # show user options from list of nodes
sn=input("Enter start node:\n") # user must enter start and end nodes
en=input("Enter end node:\n")

if sn in nodelist and en in nodelist:   # make sure the nodes entered exist
    if en != sn:    # If nodes exist and are unique from each other
        nw = network(data, nodelist, sn, en)
        print(nw.dist_meas())
    else:   # Distance between a node and itself is 0
        print("Path length = 0")
else:   # nodes don't exist
    print("One or more of these nodes do not exist")
