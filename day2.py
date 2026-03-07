# Tip calculator

print("Welcome to the tip calculator")
total = int(input("What was the total bill?: "))
tip = int(input("How much tip would you like to give?: 10, 15 or 20: "))
tip = (tip / 100) + 1
people = int(input("How many people to split the bill?: "))
value = ((total * tip) / people)
print(f"Each person should pay: $ {value}")
