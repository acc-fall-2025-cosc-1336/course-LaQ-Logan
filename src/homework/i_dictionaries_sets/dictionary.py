widgets = {} #This is an empty dictionary to store inventory items

def remove_inventory_widget(inventory_dict, widget_name): #will remove a widget from the inventory dictionary
    if widget_name in inventory_dict: #check if the widget exists in the inventory
        del inventory_dict[widget_name] #delete the widget from the inventory
        return "Record deleted" #return confirmation message for the deletion
    else:
        return "Item not found" #return message if the widget was not found
    
def add_inventory(inventory_dict, widget_name, quantity): #will add or update a widget in the inventory dictionary
    if widget_name in inventory_dict: #check if the widget already exists in the inventory
        inventory_dict[widget_name] += quantity #update the quantity of the existing widget
    else:
        inventory_dict[widget_name] = quantity #add the new widget to the inventory with the specified quantity

def display_menu(): #will display the menu options
    print("Inventory Menu ( Please select an option ):")
    print("1. Add or Update Item")
    print("2. Delete Item")
    print("3. Exit Menu")

    
def run_menu(): #will run the menu and get user input
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
        handle_choice(choice)

        if choice != "3": #if the choice is not to exit the menu then ask to continue
            if not ask_to_continue():
                print("Exiting program.")
                break


def handle_choice(choice):  # handle user's choice
    if choice == "1":
        try:
            add_or_update_item()  # call the add/update function
        except ValueError:
            print("Invalid input. Quantity must be a number.") #handle invalid  input

    elif choice == "2":
        try:
            delete_item()  # call the delete function
        except ValueError:
            print("Invalid input.") #handle invalid  input

    elif choice == "3":
        print("Exiting program.")
    else:
        print("Invalid choice. Please try again.")
        


def add_or_update_item(): #will add or update an item in the inventory
    widget_name = input("Enter widget name: ") #this is the name of the widget to add or update
    quantity = int(input("Enter quantity: "))  # raises ValueError if not a number
    add_inventory(widgets, widget_name, quantity) #call the add_inventory function ( inventory dict, widget name, quantity)
    print("Item added or updated.") #print confirmation message for addition or update
    print("Current inventory:", widgets) #print the current inventory after addition or update

def delete_item(): #will delete an item from the inventory
    widget_name = input("Enter widget name to delete: ") #this is the name of the widget to delete
    message = remove_inventory_widget(widgets, widget_name) #call the remove_inventory_widget function ( inventory dict, widget name)
    print(message) #print the result message from the deletion attempt
    print("Current inventory:", widgets) #print the current inventory after deletion attempt


def ask_to_continue(): #ask the user if they want to continue using the menu
    while True:
        again = input("Do you want to select another option? (y/n): ").lower() #get user input and convert to lowercase
        if again == 'y':
            return True #continue using the menu
        elif again == 'n':
            return False #exit the menu
        else:
            print("Invalid input. Please enter 'y' or 'n'.") #handle invalid input
