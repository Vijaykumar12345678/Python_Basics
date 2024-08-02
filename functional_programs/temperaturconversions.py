'''

@Author:Vijay Kumar M N
@Date: 2024-08-1
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-1
@Title : python program to convert the temperature.

'''
class Util:
    @staticmethod
    def Celsius_to_Fahrenheit(temperature):
        """
        Description:

        Converts a temperature from Celsius to Fahrenheit.
        
        Parameters:
        temperature :float The temperature in Celsius to be converted.
        
        Returns:
        str: The converted temperature in Fahrenheit, formatted to 2 decimal places.
        """
        fahrenheit = (temperature * 9/5) + 32 
        return f"The temperature in Fahrenheit is {fahrenheit:.2f}°F"

    def Fahrenheit_to_Celsius(temperature):
        """
        Description
        Converts a temperature from Fahrenheit to Celsius.
        
        Parameters:
        temperature :float The temperature in Fahrenheit to be converted.
        
        Returns:
        str: The converted temperature in Celsius, formatted to 2 decimal places.
        """
        celsius = (temperature - 32) * 5/9
        return f"The temperature in Celsius is {celsius:.2f}°C"

    def main():
   
        choice = int(input("\nPress 1 to convert Celsius to Fahrenheit"
                       "\nPress 2 to convert Fahrenheit to Celsius\n"))

        if choice == 1:
            temp = float(input("Enter the temperature in Celsius: "))
            result = Util.Celsius_to_Fahrenheit(temp)
            print(result)
        elif choice == 2:
            temp = float(input("Enter the temperature in Fahrenheit: "))
            result = Util.Fahrenheit_to_Celsius(temp)
            print(result)
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    Util.main()
