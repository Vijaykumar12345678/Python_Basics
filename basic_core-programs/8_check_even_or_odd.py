'''

@Author:Vijay Kumar M N
@Date: 2024-07-29
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-29
@Title : python program to check the given number is even or odd.

'''
def check_even_or_odd(number):
    """
    Description:
    Checks if a given number is even or odd.

    Parameters:
    number: interger The number to be checked.

    Returns:
    str: A message indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"The given number is Even: {number}"
    else:
        return f"The given number is Odd: {number}"

def main():
    number = int(input("Enter the number to check: "))
    result = check_even_or_odd(number)
    print(result)
    
if __name__ == "__main__":
    main()
