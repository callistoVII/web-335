# Web 335
# Date: 06/29/2025
# File Name: nielsen_lemonadeStandSchedule.py
# Description: A simple python program to manage weekly schedule for lemonade stand

# list of tasks for running the stand
tasks = [
	"Restock lemons, cups, and sugar",
	"Clean lemonade stand thoroughly",
	"Social media posts to garner business",
	"Balance sales logs, check inventory, and make bank run",
	"Brainstorm flavor ideas for specials"
]

# Print all tasks
print("Weekly Tasks to Keep The Stand Running Smoothly:")
for task in tasks:
	print(f"- {task}")

print("\n--- Weekly Schedule ---")

# Days of week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Assign tasks to weekdays, denote that weekends are for rest days
for i, day in enumerate(days):
	if day in ["Saturday", "Sunday"]:
		print(f"{day}: Day Off. Get some R&R and come back ready to slay on Monday!")
	else:
		print(f"{day}: {tasks[i % len(tasks)]}") # used the Modulus operator from w3schools 