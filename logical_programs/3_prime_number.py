'''

@Author:Vijay Kumar M N
@Date: 2024-07-31
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-31
@Title : python program to check prime number or not.
'''

def is_prime_number(n):
    """
    Determine if the given number n is a prime number.
    
    A prime number is a positive integer greater than 1 that is only divisible
    by 1 and itself. 0 and 1 are not prime numbers. The number 2 is the only
    even prime number.

    Parameters:
    n :integer The number to be checked for being a prime number.

    Returns:
    bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1 ):
        if n % i == 0:
            return False
    return True

def main():
    #userinput
    number = int(input("Enter the number to check if it is a prime number: "))
    if is_prime_number(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()
