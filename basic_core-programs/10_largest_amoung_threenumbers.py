'''

@Author:Vijay Kumar M N
@Date: 2024-07-29
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-29
@Title : python program to check largest amoung three numbers.

'''
def largest_among_three_numbers(first_number, second_number, third_number):
    """
    Description:
    Determines the largest number among three given numbers.

    Parameters:
    first_number (int): The first number.
    second_number (int): The second number.
    third_number (int): The third number.

    Returns:
    str: A message indicating which number is the largest among the three.
    """
    if first_number > second_number and first_number > third_number:
        return f"The largest among the three numbers is {first_number}"
    elif second_number > first_number and second_number > third_number:
        return f"The largest among the three numbers is {second_number}"
    else:
        return f"The largest among the three numbers is {third_number}"

def main():
   
    
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))
        
    result = largest_among_three_numbers(first_number, second_number, third_number)
    print(result)
    
if __name__ == "__main__":
    main()
