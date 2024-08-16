
'''

@Author:Vijay Kumar M N
@Date: 2024-07-29
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-29
@Title : python program to find quotient and remainder.

'''
def compute_quotient_remainder(dividend, divisor):
    """
    description
    Computes the quotient and remainder of the division of two numbers.

    Parameters:
    dividend (int): The number to be divided.
    divisor (int): The number by which to divide.

    Returns:
    tuple: A tuple containing the quotient and remainder.
    """
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

def main():
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))

    if divisor == 0:
        print("Error: Division by zero is not allowed.")
    else:
        # Calculate quotient and remainder
        quotient, remainder = compute_quotient_remainder(dividend, divisor)
            
        print(f"The quotient of {dividend} divided by {divisor} is {quotient}")
        print(f"The remainder of {dividend} divided by {divisor} is {remainder}")
    
if __name__ == "__main__":
    main()
