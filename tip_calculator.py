print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

pct = int(input("What percentage tip would you like to use? 15, 18, or 20? "))

people = int(input("How many people will split the bill? "))

tip = float(pct/100)

bill_w_tip = bill + (bill * tip)

individual_bill = round(bill_w_tip / people, 2)

message = f"Each person must pay ${individual_bill}"

print(message)