'''

@Author:Vijay Kumar M N
@Date: 2024-07-29
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-29
@Title : python program to swap the two numbers.

'''
def swap_without_temp(first_number, second_number):
    """
    decsription
    Swaps two numbers without using a temporary variable.

    Parameters:
    first_number : The first number.
    second_number: The second number.

    Returns:
    first number and second number in float
    """
    first_number = first_number + second_number
    second_number = first_number - second_number
    first_number = first_number - second_number
    return first_number, second_number

def main():
   
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
        
    first_number, second_number = swap_without_temp(first_number, second_number)

    print(f"After swapping: FirstNumber = {first_number}, SecondNumber = {second_number}")
   

if __name__ == "__main__":
    main()
