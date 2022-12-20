#Sorting List
import sys

sorter = []
excluder = []
sortChoice = 0
#1st parameter will be a variable list of numbers
#2nd parameter will be one of the following commands (asc, desc, or none)

def Msort(toSort):
    toSort1 = []
    toSort2 = []
    toSort3 = []
    length = len(toSort)
    
    if length <= 2:
        if toSort[0] <= toSort[length-1]:
            return toSort
        else:
            x = toSort[0]
            toSort[0] = toSort[length-1]
            toSort[1] = x
            return toSort
            
    
    if (length % 2) == 0:
        half = int((length / 2))
    else:
        half = int(length // 2)
    #Two arrays(0 through half) and (half+1 through len)
    y = 0
    for y in range(half):
        toSort1.append(toSort[y])
        

    for z in range(half, length):
        toSort2.append(toSort[z])
        
        
    toSort1 = Qsort(toSort1)
    toSort2 = Qsort(toSort2)
    
    #Sort Check
    #Create third array with lowest value of each array
    
    pos1 = 0
    pos2 = 0
    pos3 = 0
    
    #Run through each position in the array, compare to second array, and add to third array based on lowest value
    for pos3 in range(pos3, length):
        if pos1 < len(toSort1) and pos2 < len(toSort2):
            if toSort1[pos1] <= toSort2[pos2]:
                toSort3.append(toSort1[pos1])
                pos1 += 1
            elif toSort1[pos1] > toSort2[pos2]:
                toSort3.append(toSort2[pos2])
                pos2 +=1
        else:
            
            if pos1 < len(toSort1):
                for pos1 in range(pos1, len(toSort1)):
                    toSort3.append(toSort1[pos1])
                    pos3 += 1
            if pos2 < len(toSort2):
                for pos2 in range(pos2, len(toSort2)):  
                    toSort3.append(toSort2[pos2])
                    pos3 += 1
        if pos3 >= length:
            break                  
    return toSort3
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Prompt user for a list of numbers separated by a comma (,)
print("Sorting List")
userList = input("Please provide a list of numbers to sort using the ',' to separate each individual value.\nExample: 1, 2, 3, 4\n")

#Assign each value to an array using the comma to separate each position
val = userList.split(",")

#If there are no commas provide print their input back and claim it is sorted with respect to all commas
if(len(val) <= 1):
    print("No commas detected, therefore this is the sorted list: {}".format(userList))
    sys.exit()
    
#Prompt user for the command they want to run, presenting the three commands (asc, desc, or none)
#If user enters non command, refuse to continue until a proper command is submitted
while sortChoice == 0:
    com = input("Please choose a function for the list. The options are abbreviated respectively for Ascending Sort, Descending Sort, or No Sort.\n 1: asc\n 2: desc\n 3: none\n")
    for x in val:
        try:
            sorter.append(int(x))
        except:
            excluder.append(x)
    match com:
        case "1":
            sorter = Msort(sorter)
            sortChoice == 1
            print("Here are the sorted values\n{}".format(sorter))
            break
        case "2":
            sorter = Msort(sorter)
            sorter.reverse()
            sortChoice == 2
            print("Here are the reverse sorted values\n{}".format(sorter))
            break
        case "3":
            sortChoice == 3
            print("Here are your values, untouched\n{}".format(sorter))
            break
        case _:
            sortChoice == 0
            print("Hmm, try that again...\n{}".format(sorter))

print("Excluded list: {}".format(excluder))








    
