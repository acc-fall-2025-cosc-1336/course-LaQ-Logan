dna_lists = [ # nested lists representing DNA sequence samples
    ['T','T','T','C','C','A','T','T','T','A'], 
    ['G','A','T','T','C','A','T','T','T','C'],
    ['T','T','T','C','C','A','T','T','T','T'],
    ['G','T','T','C','C','A','T','T','T','A']
]


def display_menu(): # will show the menu options
    print("Sample DNA sequences for p-distance") # display sample DNA lists to user
    print("List 1:", dna_lists[0]) 
    print("List 2:", dna_lists[1])
    print("List 3:", dna_lists[2])
    print("List 4:", dna_lists[3])
    print()  # blank line for spacing
    
    print("Menu (Select an Option):")
    print("1. Show p-distance matrix")
    print("2. Exit")


def run_menu(): # will diplay the menu and handle user choices
    while True:
        display_menu()
        choice = input("Enter your choice, option 1 or 2: ")
        print()  # blank line for spacing
        if handle_choice(choice):
            break

def handle_choice(choice): # will process the user choice and return their result or exit 
    if choice == '1':
        print("Calculating p-distance matrix...")
        
        matrix = get_p_distance_matrix(dna_lists) #will calculate the p-distance matrix
        print_matrix(matrix)

        while True:
            again = input("Do you want to go back to the menu? (yes/no): ").strip().lower() #go back to menu or exit
            if again in ['yes', 'y']: #the user wants to go back to the menu
                return False  # go back to menu
            elif again in ['no', 'n']:  #user exits program
                print("Exiting program. Goodbye!")
                return True   # exit program
            else:
                print("Invalid input. Please type 'yes' or 'no'.") #invalid input, ask again
                
    elif choice == '2':
        print("Exiting program. Goodbye!")
        return True  # exit program
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return False  # invalid → go back to menu


def print_matrix(matrix): # will print the p-distance matrix in formatted way

    for row in matrix: # iterate through each row of the matrix
        formatted = [] # list to hold formatted string values
        for value in row:  # iterate through each value in the row
            formatted.append(f"{value:.5f}") # format each value to 5 decimal places
        print(" ".join(formatted)) # join formatted values with space and print




def get_p_distance(list1, list2): # calculates the p-distance between two lists
    differences = 0 # initialize difference counter 
    for i in range(len(list1)): # iterate through both lists and count differences
        if list1[i] != list2[i]: # list values differ at this position
            differences += 1 # increase difference count by 1

    return differences / len(list1) # return p-distance as differences divided by length of lists




def get_p_distance_matrix(list_of_lists): # generates a p-distance matrix for a list of lists
    size = len(list_of_lists) # size of the matrix is length of the list of lists
    matrix = [] # initialize empty matrix

    for i in range(size): # iterate through each list to create matrix rows
        row = [] # initialize empty row
        for j in range(size): # iterate through each list to create matrix columns
            dist = get_p_distance(list_of_lists[i], list_of_lists[j]) # calculate p-distance between two lists
            row.append(dist) # add p-distance to the current row
        matrix.append(row) # add completed row to the matrix

    return matrix # return the completed p-distance matrix





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