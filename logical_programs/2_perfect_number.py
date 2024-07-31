'''

@Author:Vijay Kumar M N
@Date: 2024-07-31
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-31
@Title : python program to Check the number is perfect number or not.
'''

def is_perfect_number(n):
    """
    Description:
    Determine if the given number n is a perfect number.
    
    A perfect number is a positive integer that is equal to the sum of its 
    positive divisors, excluding itself.

    Parameters:
    n : integer The number to be checked for being a perfect number.

    Returns:
    bool: True if n is a perfect number, False otherwise.
    """
    # Calculate the sum of all divisors of n expect itself
    sum_of_divisors = sum(i for i in range(1, int(n/2) + 1) if n % i == 0)
   
    return sum_of_divisors == n

def main():
   
    # user input
    number = int(input("Enter the number to check if it is a perfect number: "))
   
    if is_perfect_number(number):
  
        print(f"{number} is a perfect number.")
    else:
        
        print(f"{number} is not a perfect number.")


if __name__ == "__main__":
    main()
