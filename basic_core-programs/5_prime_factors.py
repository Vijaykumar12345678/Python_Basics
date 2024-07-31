'''

@Author:Vijay Kumar M N
@Date: 2024-07-29
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-29
@Title : python program to Computes the prime factorization.

'''
def prime_factors(n):
    """
    Description:
    Computes the prime factors of a given number.

    Parameters:
    n : integer The number for which to find the prime factors.

    Returns:
    list: A list containing the prime factors of the number.
    """
    factors = []
    i = 2
    
    while i * i <= n:
        while (n % i) == 0:
            factors.append(i)
            n //= i
        i += 1
    
    if n > 1:
        factors.append(n)
    
    return factors

def main():
   
    number = int(input("Enter the number: "))
    if number <= 0:
        print("Please enter a positive integer.")
        return
        
    result = prime_factors(number)
    print(f"Prime factors: {result}")
    
if __name__ == "__main__":
    main()
