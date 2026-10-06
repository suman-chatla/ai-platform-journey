bill = float(input("Enter the total bill amount: $ "))
tax = 7.85
tip_percentage = int(input("what is the tip percent you would like to give 10 12 18: "))
persons = int(input("How many people to split the bill? "))

bill_amount = bill + (bill * tax / 100)
tip_amount= bill *(tip_percentage/100)

total_amount = bill_amount + tip_amount
split_amount = total_amount / persons

print(f"tax amount: ${bill * tax / 100:.2f}")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount: ${total_amount:.2f}")
print(f"Amount per person: ${split_amount:.2f}")
