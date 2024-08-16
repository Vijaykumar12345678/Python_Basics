'''

@Author:Vijay Kumar M N
@Date: 2024-08-1
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-1
@Title : python program to find the square root.

'''
class Util:
    @staticmethod
    def sqrt(c):
        """
        Description:
        Compute the square root of a nonnegative number c using Newton's method.
        
        Parameters:
        c :float The nonnegative number to compute the square root of.
        
        Returns:
        float: The computed square root of c.
        """
        
        
      
        t = c
        epsilon = 1e-15
        
        while abs(t - c / t) > epsilon * t:
            t = (c / t+t ) / 2
        
        return t

    def main():
        # user input
        number = float(input("Enter a nonnegative number to compute its square root: "))
    
        result = Util.sqrt(number)
        print(f"The square root of {number} is approximately {result:.15f}")
    
if __name__ == "__main__":
    Util.main()
