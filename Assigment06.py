#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   KKniestedt, 11/21/2016, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

objFile = "Todo.txt"
strData = ""
dicRow = {}
lstTable = []

class BGProcessing:
    @staticmethod
    def loadData(objFile):
        ### This function loads the dictionary file on initial load ###
        f = open(objFile, "r")
        for line in f:
            (key, val) = line.split(",")  # open the file, look for two objects, read into key, val
            dicRow[key] = val.strip()  # append to dictionary dicRow as [key]=val
        f.close()  # close the file
        print(dicRow)

    def pause():
        ### This function pauses the program and asks the user to press enter ###
        input("Press enter to continue")

    def showMenu():
        ### This function shows the menu ###
        print("""
            Menu of Options
            1) Show current data
            2) Add a new item.
            3) Remove an existing item.
            4) Save Data to File
            5) Exit Program
            """)


    def showItems():
        ### This function shows all items in the list ###
        print("Current items in the list: ")
        print("[Item: Priority]\n")
        for strKey, strVal in dicRow.items(): print(strKey + ": " + strVal)  # for each value in the dict, print it

    def addItems(newitem,newpriority):
        ### This function queries the user for new tasks and adds them to the dictionary ###
        dicRow[newitem] = newpriority  # append to dictionary
        print("Okay, got it. Here is the new table:\n")  # print the dict with the new line appended
        for strKey, strVal in dicRow.items(): print(strKey + ": " + strVal)

    def removeItems(strKeytoDel):
        ### This function queries the user for tasks to remove from the dictionary ###
        if (strKeytoDel in dicRow):
            del dicRow[strKeytoDel]  # look for the str before trying to del
            print()
            print("The task called '" + strKeytoDel + "' has been removed")
        else:
            print("I'm sorry, I could not find that item\n")  # if it isn't there, inform the user

    def saveTasks(objFile):
        ### This function saves the dictionary to the storage ###
        f = open(objFile, "a")  # open the file with r/w access
        f.truncate(0)  # erase the data so we don't have duplicate info
        for strKey, strVal in dicRow.items(): f.write(strKey + "," + strVal + "\n")  # write each line of the dict
        f.close()  # close it out
        print("Okay, everything is saved\n")

class InOut:
    @staticmethod
    def pickMenu():
        strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
        return strChoice

    def getNewItems():
        newItem = input("What is the new item you'd like to add? ")  # capture the new item and pri
        newPriority = input("What is the priority? (high/low) ")
        return newItem, newPriority

    def getRemItems():
        for strKey, strVal in dicRow.items(): print(strKey + ": " + strVal)  # print the table for the user
        strKeytoDel = input("Type the name of the item you would like to remove: ")
        return strKeytoDel

# Step 1
    # When the program starts, load the any data you have
    # in a text file called ToDo.txt into a python Dictionary.

BGProcessing.loadData(objFile)

# Step 2 - Display a menu of choices to the user
while(True):
    BGProcessing.showMenu()
    strChoice = InOut.pickMenu()
    print()

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        BGProcessing.showItems()
        BGProcessing.pause()
        continue
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        newItem, newPriority = InOut.getNewItems()
        BGProcessing.addItems(newItem, newPriority)
        BGProcessing.pause()
        continue
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        strKeyToDel = InOut.getRemItems()
        BGProcessing.removeItems(strKeyToDel)
        BGProcessing.pause()
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        BGProcessing.saveTasks(objFile)
        BGProcessing.pause()
        continue
    elif (strChoice == '5'):
        print("See you later!") #say goodbye
        break #and Exit the program

