'''

@Author:Vijay Kumar M N
@Date: 2024-07-31
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-07-31
@Title : python program to find the day.

'''
class util:
    @staticmethod
    def dayofweeks(month,day,year):
        """
        Description :
        function that takes a date as input and prints the day of the week that date falls on
        parameters:
        month:integer the month of the day
        day:the day of the month
        year: The year
        return:
        integer"""
        y1 = year-(14-month)//12
        x = y1 + y1//4 - y1//100 + y1//400
        m1 = month + 12 * ((14-month)//12)-2
        d1 = (day + x + 31*m1// 12) % 7
        return d1
    def main():
        year=int(input("Enter the year"))
        month=int(input("Enter the month"))
        date=int(input("Enter the present date"))
        days=util.dayofweeks(month,date,year)
        day={0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
        print(day[days])
        
if __name__=="__main__":
    util.main()