'''

@Author:Vijay Kumar M N
@Date: 2024-07-29
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-29
@Title : python program to check the given alphabet is vowel or consotant.

'''
def check_vowel_or_consonant(alphabet):
    """
    Description:
    Checks if a given alphabet is a vowel or a consonant.

    Parameters:
    alphabet (str): The alphabet to be checked.

    Returns:
    str: A message indicating whether the alphabet is a vowel or a consonant.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    alphabet = alphabet.lower()
    
    if alphabet in vowels:
        return "The given alphabet is a vowel."
    else:
        return "The given alphabet is a consonant."

def main():
   
    alphabet = input("Enter the alphabet to check if it is a vowel or consonant: ")
    
    if len(alphabet) != 1 or not alphabet.isalpha():
        print("Invalid input. Please enter a single alphabet character.")
        return
    
    result = check_vowel_or_consonant(alphabet)
    print(result)

if __name__ == "__main__":
    main()
