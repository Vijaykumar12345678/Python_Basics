'''

@Author:Vijay Kumar M N
@Date: 2024-08-1
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-1
@Title : python program to convert decimal to binary.

'''
def decimal_to_binary(n):
    """
    description:
    Convert a decimal number to binary using manual conversion.
    
    Parameters:
    n : integer The decimal number to convert.
    
    Returns:
    str: The binary representation of the number, padded to 32 bits.
    """
  
        
    if n == 0:
        return "0"  
    binary_representation = ""
    while n > 0:
        binary_representation = str(n % 2) + binary_representation
        n //= 2
    
    return binary_representation  
def main():
    number = int(input("Enter a nonnegative decimal number: "))
    binary_representation = decimal_to_binary(number)
    print(f"The binary representation of {number} is: {binary_representation}")
if __name__=="__main__":
    main()