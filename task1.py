#!python3
 
"""
##### Task 1
The bank calculates the amount of interest you earn using the simple interest formula:
interest = principal * rate * #days in the month / 365

Ask the user to enter the amount of their principal, the number of days in the month the rate of interest expressed as a percentage.  Calculate the amount of interest they would be paid.

example:
Enter your amount: 100
Enter the rate: 2.5
Enter the # of days in the month: 30
You earned $0.2 interest. 
(2 points) 
"""
import math
principal = input("please enter the amount you would like to deposit.")
principal = int(principal)
rate = input("please enter the rate")
rate = float(rate)
rate = rate/100
month = input("please enter the days in a month")
month = int(month)
interest = (principal*rate*month/365)
interest = round(interest, 1)
print(f"You earned ${interest} interest.")