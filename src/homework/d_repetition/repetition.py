def get_factorial(n): #will calculate the factorial of a number
    result = 1 
    for i in range(1, n + 1): # loop from 1 to n
        result *= i # multiply result by i
    return result # return the factorial result

def sum_odd_numbers(n): #will calculate the sum of odd numbers up to n
    total = 0 
    i = 1 # start with the first odd number
    while i <= n: #loop until i exceeds n
        total += i # add the odd number to total
        i += 2   # move to next odd number
    return total

def display_menu(): #will display the menu options
    print("Menu (Select an Option):")
    print("1. Factorial")
    print("2. Sum Odd Numbers")
    print("3. Exit")
    
    
def run_menu(): #will run the menu and get user input
    while True: # loop until user chooses to exit
        display_menu()
        choice = input("Enter your choice (1-3): ")
        if handle_choice(choice):
            break

def handle_choice(choice): #will handle the user's choice
    if choice == '1':
        try:
            number = int(input("Enter a number (1-9): "))
            if 0 < number < 10: # check if number is in range > 0 and < 10
                print(f"Factorial of {number} is {get_factorial(number)}") # display the factorial result
            else:
                print("Number must be between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a whole number between 1-9.") # handle incorrect input

    elif choice == '2':
        try:
            number = int(input("Enter a number (1-99): "))
            if 0 < number < 100: # check if number is in range > 0 and < 100
                print(f"Sum of odd numbers up to {number} is {sum_odd_numbers(number)}") # display the sum of odd numbers result
            else:
                print("Number must be between 1 and 99.")
        except ValueError:
            print("Invalid input. Please enter a whole number between 1-99.") # handle incorrect input

    elif choice == '3':
        print("Exiting the program.") # exit message
        return True  # signal to exit the loop

    else:
        print("Invalid choice. Please try again with options 1-3.") # handle invalid menu choice
    return False # continue the loop
        