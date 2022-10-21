# brief intro
print("++++++++++++ TAX CALCULATOR +++++++++++")
print("Welcome to Tax calculator")
# get data from user
amount = float(input("What is the total bill: $"))
tax_percent = float(input("What percentage tip wopuld you like to give? (10, 15, 20 or 25): "))
people = int(input("How many people to split the bill? "))
# ytilize the gotten data
tip = amount * (tax_percent / 100)
bill = (amount + tip) / people
processed_bill = round(bill, 2)
# give the output
print("Each person would pay $%.2f" % processed_bill)