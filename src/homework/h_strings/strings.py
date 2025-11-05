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
            dna1 = input("Enter the first DNA string: ") #get first DNA string from user
            dna2 = input("Enter the second DNA string: ") #get second DNA string from user
            if len(dna1) != len(dna2): #check if the lengths of the two strings are equal
                print("Error: Strings must be of the same length.") 
            else:
                print(f"Hamming Distance: {get_hamming_distance(dna1, dna2)}") #calculate and display the hamming distance
        except ValueError:
            print("Invalid input. Please enter valid DNA strings consisting of A, T, C, and G only.")

    elif choice == '2':
        try:
            dna = input("Enter a DNA string (A, T, C, G): ") #get DNA string from user
            print(f"DNA Complement: {get_dna_complement(dna)}") #calculate and display the DNA complement
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

    while index < len(dna1): #loop through each character in the strings
        if dna1[index] != dna2[index]: #compare characters at the same position
            distance += 1 #found a difference, increment distance +1
        index += 1  #move to the next character
    return distance 

def get_dna_complement(dna): #will calculate the DNA complement of a given DNA string
    complement = ""     #an empty string to store the complement
    index = len(dna) - 1 #start from the end of the string

    while index >= 0: #loop through the string in reverse order
        symbol = dna[index]
        if symbol == 'A': #if the symbol is A, its complement is T
            complement += 'T' #add T to the complement
        elif symbol == 'T': #if the symbol is T, its complement is A
            complement += 'A' #add A to the complement
        elif symbol == 'C': #if the symbol is C, its complement is G
            complement += 'G' #add G to the complement
        elif symbol == 'G': #if the symbol is G, its complement is C
            complement += 'C' #add C to the complement
        else:
            print("Invalid input. Please enter a valid DNA string consisting of A, T, C, and G only.")
        index -= 1
    
    return complement  #return the complement