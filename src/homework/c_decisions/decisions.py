def display_menu(): #will display the menu options
    print("Menu (Select an Option):")
    print("1. Letter grade using if")
    print("2. Letter grade using switch")
    print("3. Exit")
    
    
def run_menu(): #will run the menu and get user input
    display_menu()
    choice = input("Enter your choice (1-3): ")
    handle_choice(choice)

def handle_choice(choice): #will handle the user's choice
    if choice == '1':
        try:
            grade = float(input("Enter the numeric grade: "))
            letter = letter_grade_if(grade)
            print(f"Letter grade (if): {letter}")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
            return # Exit the function if input is invalid
    elif choice == '2':
        try:
            grade = float(input("Enter the numeric grade: "))
            letter = letter_grade_switch(grade)
            print(f"Letter grade (switch): {letter}")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
            return # Exit the function if input is invalid
    elif choice == '3':
        print("Exiting the program.")
    else:
        print("Invalid choice. Please try again.")

def letter_grade_if(grade): #will return the letter grade using if statements
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'
    
def letter_grade_switch(grade): #will return the letter grade using a switch-case structure
    switcher = {
        range (90,101): 'A',
        range (80,90): 'B',
        range (70,80): 'C',
        range (60,70): 'D',
        range (0,60): 'F'
    }
    for key in switcher:
        if grade in key:
            return switcher[key]
    return 'Invalid grade'  # In case the grade is out of range
