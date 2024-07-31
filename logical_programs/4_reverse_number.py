'''

@Author:Vijay Kumar M N
@Date: 2024-07-31
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-31
@Title : python program to reverse a number.
'''

def reverse_number(n):
    """
    Reverse the digits of the given number n.
    
    This function reverses the digits of the input number by following these steps:
    1. Calculate the remainder of the number using the modulo operation.
    2. Multiply the variable 'reverse' by 10 and add the remainder to it.
    3. Divide the number by 10 and repeat the steps until the number becomes 0.

    Parameters:
    n : The number to be reversed.

    Returns:
    int: The reversed number.
    """
    reverse = 0
    while n > 0:
        remainder = n % 10
        reverse = (reverse * 10) + remainder  
        n = n // 10              
    return reverse

def main():
   
    # user input
    number = int(input("Enter the number to be reversed: "))
    reversed_number = reverse_number(number)
    print(f"The reversed number is: {reversed_number}")

if __name__ == "__main__":
    main()
