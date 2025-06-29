# Web 335
# Date: 06/15/2025
# File Name: nielsen_lemonadeStand.py
# Description: Lemonade Stand Economics 101

# Define total cost function for lemonade stand
def calculate_cost(lemons_cost, sugar_cost):
	return lemons_cost + sugar_cost

# Define profit calculation
def calculate_profit(lemons_cost, sugar_cost, selling_price):
	total_cost = calculate_cost(lemons_cost, sugar_cost)
	return selling_price - total_cost

# Testing variables
lemons = 1.25
sugar = 2.50
selling_price = 6.50

# Cost result
cost = calculate_cost(lemons, sugar)
cost_output = str(lemons) + " + " + str(sugar) + " = " + str(cost)

# Profit result
profit = calculate_profit(lemons, sugar, selling_price)
profit_output = "Selling price: " + str(selling_price) + " - Cost: " + str(cost) + " = Profit: " + str(profit)

# Print results
print("Cost breakdown: ", cost_output)
print("Profit Analysis: ", profit_output)

