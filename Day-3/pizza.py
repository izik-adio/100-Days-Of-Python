"""
Pizza Deliveries
"""
print("Welcome to Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra chees? Y or N ")
SMALL_PIZZA = 15
MEDIUM_PIZZA = 25
LARRGE_PIZZA = 40
PEPPERONI = 5
PEPPERONI_SMAIL = 2
CHEESE  = 4
BILL = 0
if size == "S":
    BILL += 15
elif size == "M":
    BILL += 25
elif size == "L":
    BILL += 40
if add_pepperoni == "Y":
    if size == "S":
        BILL += 2
    else:
        BILL += 5

if CHEESE == "Y":
    BILL += 4
print(f"Your final bill is ${BILL}")
