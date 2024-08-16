'''

@Author:Vijay Kumar M N
@Date: 2024-08-1
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-1
@Title : python program to find the monthly installment.

'''
class Util:
    @staticmethod
    def monthlypayment(principal, year, rate):
        """
        Description:
        Calculate the monthly payment for a loan.

        Parameters:
        principal (float): The principal loan amount.
        year (int): The number of years over which the loan will be repaid.
        rate (float): The annual interest rate in percentage.

        Returns:
        str: A string indicating the monthly payment.
        """
        n = 12 * year  
        r = rate / (12 * 100)  
        payment = (principal * r) / (1 - (1 + r) ** -n)
        return f"The monthly payment is {payment:.2f}"  
    def main():
        
        year = int(input("Enter the number of years: ")) 
        principal = float(input("Enter the principal amount: "))  
        rate = float(input("Enter the annual interest rate (in %): "))  
        result = Util.monthlypayment(principal, year, rate)
        print(result)

if __name__ == "__main__":
    Util.main()  