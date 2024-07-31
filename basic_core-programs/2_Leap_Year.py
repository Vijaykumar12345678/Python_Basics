'''

@Author:Vijay Kumar M N
@Date: 2024-07-29
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-29
@Title : python program to check leap year or not.

'''
def is_leap_year(year):
    """
    Description:Checks if a given year is a leap year.

    Parameters:
    year: integer The year to check.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    
    year = input("Enter the year to check if it is a leap year or not: ")
    
    # Ensure the input year is a valid 4-digit number
    while not (year.isdigit() and len(year) == 4):
        year = input("Invalid input. Please enter a valid 4-digit year: ")
    
    year = int(year)
    
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()
