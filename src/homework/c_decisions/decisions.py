def get_options_ratio(option, total): # option/total
    return option / total # ratio 

def get_faculty_rating(ratio): # ratio -> rating
    if 0 <= ratio < 0.6:
        return "Unacceptable"
    elif ratio >= 0.6 and ratio <= 0.7:
        return "Needs Improvement"
    elif ratio > 0.7 and ratio <= 0.8:
        return "Good"
    elif ratio > 0.8 and ratio < 0.9:
        return "Very Good"
    elif ratio >= 0.9 and ratio <= 1:
        return "Excellent"
    else:
        return "Invalid Ratio, Please enter a valid ratio between 0 and 1"