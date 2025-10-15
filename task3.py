#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""

price1 = input("Enter the first price.")
price2 = input("Enter the second price")
price3 = input("Enter the third price.")
price4 = input("Enter the fourth price.")
price5 = input("Enter the fifth price.")

price1 = float(price1)
price2 = float(price2)
price3 = float(price3)
price4 = float(price4)
price5 = float(price5)
total = price1+price2+price3+price4+price5

taxtotal = total*0.12
taxtotal = round(taxtotal, 2)


final_total = total+taxtotal
print(f"your subtotal is ${total} and your taxes total to ${taxtotal} for a total of ${final_total} ")

