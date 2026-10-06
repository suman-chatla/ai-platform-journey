bill = float(input("Enter the total bill amount: $ "))
tip_percentage = int(input("what is the tip percent you would like to give 10 12 18: "))
persons = int(input("How many people to split the bill? "))

tip_amount= bill *(tip_percentage/100)

total_amount = bill + tip_amount
split_amount = total_amount / persons


print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount: ${total_amount:.2f}")
print(f"Amount per person: ${split_amount:.2f}")
