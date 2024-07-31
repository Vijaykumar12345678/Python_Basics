'''

@Author:Vijay Kumar M N
@Date: 2024-07-31
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-31
@Title : python program to generate the fibonacci series.
'''
def fibonacci_series(n):
    """
    Description:
     The program will generate a finonacci series where it will add last term and last before to make the next term
     Parameters:
     n:integer till where it should generate the fibonacci series
     returns:a list of fibonacci series.
     """
    # Initialize Fibonacci series
    fib_sequence = [0, 1]
    
    
    for i in range(2, n+1):
        
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
   
    return fib_sequence
def main():
    # user input
     number=int(input("Enter the till where the fibonacci series to print: "))
     print(f"Fibonacci series up to {number} terms: {fibonacci_series(number)}")

if __name__=="__main__":
    main()
