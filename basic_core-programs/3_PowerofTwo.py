
'''

@Author:Vijay Kumar M N
@Date: 2024-07-29
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-29
@Title : python program to generate the power of 2 till N.

'''
def power_of_two(number):
    """
    Description:
    Prints the powers of 2 up to the given number.

    Parameters:
    number: integer The upper limit for the exponent in the power of 2 calculations.
    returns:None
    """
    
    for num in range(number + 1):
        print(f"2^{num} = {2 ** num}")

def main():
    number = int(input("Enter the number up to which you want powers of 2: "))
    if number < 0:
        print("Please enter a non-negative integer.")
    else:
        power_of_two(number)
        
if __name__ == "__main__":
    main()
