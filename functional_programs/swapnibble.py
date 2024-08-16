'''

@Author:Vijay Kumar M N
@Date: 2024-08-1
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-1
@Title : python program to convert decimal to binary and Swap nibbles and find the new number and  the resultant number is the number is a power of 2.
.  
'''
from tobinary import decimal_to_binary 
class Util:
    @staticmethod
    def swap_nibbles(n):

        binary_str =decimal_to_binary(n)      
        high_nibble = binary_str[:4]
        low_nibble = binary_str[4:]
        swapped_binary_str = low_nibble + high_nibble
        return swapped_binary_str
    def is_power_of_two(n):
        """
        Check if a number is a power of 2.
    
        Parameters:
        n (int): The number to check.
    
        Returns:
        bool: True if the number is a power of 2, otherwise False.
        """
        return (n & (n - 1)) == 0 and n != 0

def main():
    """
    Main function to read input, convert to binary, swap nibbles, and check if the result is a power of 2.
    """
    # Read integer input from the user
    number = int(input("Enter an integer: "))

    # Convert the number to binary
    #binary_representation = to_binary(number)
    #print(f"Binary representation: {binary_representation}")

    # Swap nibbles and find the new number
    swapped_number =Util.swap_nibbles(number)
    print(f"Number after swapping nibbles: {swapped_number}")

    # Check if the resultant number is a power of 2
    is_power = Util.is_power_of_two(int(swapped_number))
    print(f"Is the resultant number a power of 2? {is_power}")

if __name__ == "__main__":
    main()
