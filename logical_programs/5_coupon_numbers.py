'''

@Author:Vijay Kumar M N
@Date: 2024-07-31
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-31
@Title : python program to generate distinct ticket numbers.
'''
import random 
class CouponCollector:
    @staticmethod
    def collect_coupons(length):
        """
        Simulate the process of collecting N distinct coupon numbers.
        
        Parameters:
        N (int): The number of distinct coupon numbers to collect.
        
        Returns:
        int: The total number of random numbers generated to collect all distinct coupons.
        """
        coupons = set()

        while len(coupons) < length:
            # Generate a random number between 1 and N (inclusive)
            number = random.randint(0,9)
            coupons.add(number)
        
        return coupons

def main():
    #user input
    length=int(input("Enter the number how many numbers should be present in a ticket"))
    if length<=0:
         print("Please enter a positive integer for the number of distinct coupons.")
         length=int(input("Enter the number how many numbers should be present in a ticket"))
    coupon_number=CouponCollector.collect_coupons(length)
    coupons=""
    for distincts in coupon_number:
        print(distincts,end="")
if __name__=="__main__":
    main()