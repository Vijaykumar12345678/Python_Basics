
'''

@Author:Vijay Kumar M N
@Date: 2024-07-29
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-29
@Title : python program to print the Nth Harmonic number.

'''
def harmonic_value(number):
    """
    Description:
    Calculates the nth harmonic value.

    Parameters:
    number : The number up to which the harmonic value is to be calculated.

    Returns:
    float: The nth harmonic value.
    """
    if number < 1:
        return 0.0
    
    harmonic_sum = 0.0
    for num in range(1, number + 1):
        harmonic_sum += 1 / num
    
    return harmonic_sum

def main():
    number = int(input("Enter the number: "))
    if number < 1:
        print("Please enter a positive integer.")
    else:
        result = harmonic_value(number)
        print(f"The Harmonic Value is {result:.5f}")
    
if __name__ == "__main__":
    main()
