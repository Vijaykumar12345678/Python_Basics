import random
'''

@Author:Vijay Kumar M N
@Date: 2024-07-29
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-29
@Title : python program to find the Flip Coin and print percentage of Heads and Tails.

'''

def simulate_coin_flips(number_of_flips):
    heads = 0
    tails = 0
    """
    Description :This function takes number_of_flips as input and simulates flipping a coin that many times.
    parameter:
     number-of_filps:An integer representing the number of coin flips (or trials) to simulate
    returns:the percentage of getting heads and tails
"""
    
    for i in range(number_of_flips):
        coin = random.random()
        if coin < 0.5:
            tails += 1
        else:
            heads += 1
    
    head_percentage = float(heads / number_of_flips) * 100
    tail_percentage = float(tails / number_of_flips) * 100
    
    return head_percentage, tail_percentage

def main():
    number_of_flips = int(input("Enter the number of trials: "))
    head_percentage, tail_percentage = simulate_coin_flips(number_of_flips)
    
    print(f"The percentage of getting heads is {head_percentage:.2f}%")
    print(f"The percentage of getting tails is {tail_percentage:.2f}%")

if __name__ == "__main__":
    main()
