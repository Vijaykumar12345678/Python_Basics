'''

@Author:Vijay Kumar M N
@Date: 2024-08-01
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-01
@Title : python program to  Calculate the minimum number of notes needed to return the specified amount.

'''
def calculate_change(amount, notes):
    """
    Description:
    Calculate the minimum number of notes needed to return the specified amount.
    
    Parameters:
    amount : integer The amount of change to return.
    notes : List of available note denominations in descending order.
    
    Returns:
    tuple: A tuple containing two elements:
        
    """
    if amount == 0:
        return {}
    
    # Recursive case
    for note in notes:
        if amount >= note:
            count = amount // note
            remaining_amount = amount % note
            remaining_notes, remaining_count = calculate_change(remaining_amount, notes)
            result = {**remaining_notes, note: count}
            total_notes = count + remaining_count
            return result, total_notes

def main():
    
    notes = [1000, 500, 100, 50, 10, 5, 2, 1]
    
    amount = int(input("Enter the amount of change to be returned: "))

    if amount <= 0:
        print("Amount should be greater than 0.")
        return
    notes, total_notes = calculate_change(amount, notes)
    
    # Print the results
    print(f"Total number of notes needed: {total_notes}")
    print("Notes to be returned:")
    for note in sorted(notes.keys(), reverse=True):
        print(f"₹{note}: {notes[note]}")

if __name__ == "__main__":
    main()
