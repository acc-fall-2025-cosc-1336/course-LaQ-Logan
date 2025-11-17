from decisions import get_options_ratio, get_faculty_rating


def main():
    options = float(input("Enter the number of options: ")) # get option # from user
    total = float(input("Enter the total: ")) # get total # from user
    ratio = get_options_ratio(options, total) # calculate ratio
    rating = get_faculty_rating(ratio) # get rating based on ratio
    print(f"Faculty rating: {rating}")

    
if __name__ == "__main__":
    main()