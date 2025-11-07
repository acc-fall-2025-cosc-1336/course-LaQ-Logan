def display_menu(): # will show the menu options
    print ("\nMenu:")
    print ("1. show the list high/low values ")
    print ("2. Exit ")

def run_menu(): # will diplay the menu and handle user choices
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if handle_choice(choice):
            break

def handle_choice(choice): # will process the user choice and return their result or exit 
    if choice == '1':
        numbers_list = get_user_list() # get the user list of numbers

        lowest_value = get_lowest_list_value(numbers_list) # get the lowest value from the list
        highest_value = get_highest_list_value(numbers_list) # get the highest value from the list

        print(f"Lowest value: {lowest_value}") # display the lowest value
        print(f"Highest value: {highest_value}") # display the highest value

        return False 
    elif choice == '2': # exit the program
        print("Exiting the program.")
        return True
    else:
        print("Invalid choice. Please try again.") #handles invalid menu choice
        return False
    
def get_lowest_list_value(values): # returns the lowest value from a list of numbers
        if not values:
            return None
        lowest_value = values[0] # assume the first value is the lowest

        for current_number in values: # iterate through the list
            if current_number < lowest_value: # check if the current number is lower than the lowest found so far
                lowest_value = current_number # update the lowest value found
        
        return lowest_value
    
def get_highest_list_value(values): # returns the highest value from a list of numbers
    if not values:
        return None
    highest_value = values[0] # assume the first value is the highest

    for current_number in values: # iterate through the list
        if current_number > highest_value: # check if the current number is higher than the highest found so far
            highest_value = current_number # update the highest value found
    
    return highest_value
    
def get_valid_number(): # prompts the user for a valid whole number input
    while True:
        value_input = input("Enter a list value: ") # prompt user for input
        try:
            return int(value_input)
        except ValueError:
            print("Invalid input. Please enter a valid whole number as a value.")

def ask_to_continue(): # asks the user if they want to continue adding numbers
    while True:
        again = input("Do you want to add another number? (y/n): ").strip().lower()
        if again == 'y':
            return True
        elif again == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n' to select your choice.")

def get_user_list(): # gets a list of numbers from the user
    user_values = [] # initialize an empty list to store user values

    while True: # loop to get user input
        number = get_valid_number() # get a valid number from the user
        user_values.append(number) # add the number user enters to the list 

        if len(user_values) >= 3: # ensure at least 3 numbers are entered before asking to continue
            if not ask_to_continue(): 
                break # exit the loop if user does not want to continue adding numbers
    
    return user_values # return the list of user values 