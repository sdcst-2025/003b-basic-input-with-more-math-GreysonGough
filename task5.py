#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days
import math

population = input("please enter the current population.")
rate = input("enter the rate of growth in decimals.")
days = input("enter the number of days.")

days = int(days)
rate = float(rate)
population = float(population)

rate = rate/100
days_in_year = days/365

future_population = (population)*(1+rate)**days_in_year
future_population = float(future_population)
future_population = round(future_population)
print(f"There will be {future_population} people after {days} days")