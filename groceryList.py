# grocery list manager
import sys
groceryList = {}

# functions per option
#1 adding item
def addItems():
    while True:
        newItem = input("Enter the item you want to add: ")
        newQuantity = input("Enter how many of these items you want: ")
        if newItem and newQuantity != '': 
            if newItem not in groceryList:   
                groceryList[newItem] = newQuantity
                print ("Thank you, item(s) added!")
                return groceryList       
            
        else:
            print (f"Invalid input, please enter a valid option.\n")
            continue

#2 removing items
def removeItems():
    while True:
        print (f"Press 1 to remove a specific item.\nPress 2 to empty the entire list.\nPress Enter to return to main menu.")
        removeAnswer = input().strip()
        if removeAnswer == '1':            
            try:
                choice = input(f"\nEnter 'a' to remove all quantities.\nEnter 'b' to remove a specific amount:\n").lower().strip()
                if choice == 'a':
                    checkItem = input("Enter the item you want to remove: ").lower().strip()
                    if checkItem in groceryList.keys():
                        groceryList.pop(checkItem)
                        print (f"Item removed")
                        return groceryList            
                    else:
                        print ("Invalid input, item isn't in grocery list.")
                        break            
                
                elif choice == 'b':
                    checkItem2 = input("Enter the item you want to remove: ").lower().strip()
                    num = int(input(f"How many bits of {checkItem2} would you like to remove? : "))
                    for k, v in groceryList.items():
                        oldNum = int(v)
                        newNum = oldNum - num
                    if checkItem2 in groceryList.keys():
                        groceryList.update({checkItem2 : newNum})
                        print (f"Item removed")
                        return groceryList 

            except:
                print ("Invalid input, that item doesn't exist: ")
                continue
        
        elif removeAnswer == '2':
            groceryList.clear()
            print ("Item removed")
            return groceryList
        elif removeAnswer == '':
            break
        else:
            print ("Invalid input, please enter a valid option.")
            continue    

#3 updating items
def updateItems():
    while True:
        response = input(f"\nEnter the item you want to update: ").lower().strip()
        if response in groceryList:
            newValue = input("Enter the new quantity you want for this item: ").strip()
            groceryList[response] = newValue
            print ("Thank you, the item quantity has been updated!")
            return groceryList
        
        else:
            print ("Item not in grocery list, please add item on the main menu.")
            response1 = input("Would you like to return to the main menu? : ")
            if response1 == 'yes':
                break
            else:
                continue

#4 error handling
def carryOn():
    while True:
            response1 = input(f"\nWould you like to continue? : ").lower().strip()
            if response1 == 'yes':
                break
            elif response1 == 'no':
                sys.exit("Exiting...")
            else:
                print ("Invalid input, please enter yes or no.")
                continue

# MAIN PROGRAM LOOP #
print (f"\nWelcome to your grocery manager:", end='')

while True:     
    print (f"""\nPress 1 to add items to your grocery list.
Press 2 to remove items from your grocery list.
Press 3 to update the quantity of items for an existing item.
Press 4 to display the grocery list.
Press 5 to check whether a specific item exists in the list.
Press any other key to exit the program.
""")

# options
    option = input()

    if option == '1':
        addItems()
        carryOn()
    
    elif option == '2':
        removeItems()
        carryOn()
        continue
    
    elif option == '3':
        updateItems()
        carryOn()
        continue
    
    elif option == '4':
        print ('GROCERY LIST'.center(30, '-'))
        for k, v in groceryList.items():
            print (k.ljust(20, '.') + str(v).rjust(10))
        carryOn()

    elif option == '5':
        while True:
            userCheck = input("What item are you looking for? : ").lower().strip()
            if userCheck != '':
                if userCheck in groceryList.keys():
                    print (f"{userCheck} is in the list.")
                else:
                    print (f"{userCheck} isn't in the list.")
                break            
            else:
                print ("Invalid input, please enter a valid option.")
                continue  
    
# ERROR HANDLING RESPONSE    
    else:
        while True:
            exitResponse = input("Are you sure you want to quit? (yes/no): ").lower().strip()
            if exitResponse == 'yes':
                sys.exit("Exiting...")
            elif exitResponse == 'no':
                break
            else:
                print ("Invalid input, please enter yes or no")
                continue