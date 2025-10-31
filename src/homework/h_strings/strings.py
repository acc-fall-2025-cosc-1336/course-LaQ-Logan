def display_menu(): #will display the menu options
    print("Menu (Select an Option):")
    print("1. Hamming Distance")
    print("2. DNA Complement")
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
            dna1 = input("Enter the first DNA string: ")
            dna2 = input("Enter the second DNA string: ")
            if len(dna1) != len(dna2):
                print("Error: Strings must be of the same length.")
            else:
                print(f"Hamming Distance: {get_hamming_distance(dna1, dna2)}")
        except ValueError:
            print("Invalid input. Please enter valid DNA strings consisting of A, T, C, and G only.")

    elif choice == '2':
        try:
            dna = input("Enter a DNA string (A, T, C, G): ")
            print(f"DNA Complement: {get_dna_complement(dna)}")
        except ValueError:
            print("Invalid input. Please enter a valid DNA string consisting of A, T, C, and G only.")

    elif choice == '3':
        print("Exiting the program.") # exit message
        return True  # signal to exit the loop

    else:
        print("Invalid choice. Please try again with options 1-3.") # handle invalid menu choice
    return False # continue the loop

def get_hamming_distance(dna1, dna2): #will calculate the hamming distance between two DNA strings
    distance = 0
    index = 0

    while index < len(dna1):
        if dna1[index] != dna2[index]:
            distance += 1
        index += 1
    return distance

def get_dna_complement(dna):
    complement = ""
    index = len(dna) - 1

    while index >= 0:
        symbol = dna[index]
        if symbol == 'A':
            complement += 'T'
        elif symbol == 'T':
            complement += 'A'
        elif symbol == 'C':
            complement += 'G'
        elif symbol == 'G':
            complement += 'C'
        else:
            print("Invalid input. Please enter a valid DNA string consisting of A, T, C, and G only.")
        index -= 1
    
    return complement 