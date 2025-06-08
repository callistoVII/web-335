# Class - Web-335 Introduction to NoSQL
# Name: Nicole Nielsen
# Date: 06/08/2025
# Assignment: Exercise 2.3 Python 


print("Hello! Welcome to my simple investment program!")
invested = float(input("For this program, you will need to enter your initial investment amount by using whole numbers: "))
rate = float(input("Without using any special characters, enter the interest rate: "))

year = 0
total = invested

while total <= invested * 2 :

    total = total + total * (rate)/100
    year = year + 1
    

print("Years before your investment doubles: ",year)