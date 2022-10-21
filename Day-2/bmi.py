# Brief intro to the program
from math import floor

print('~' * 15,"BODY MASS INDEX", '~' * 15)
print("Hello user, I'm BMI~Robot🤖 "
      "\nI would help you calculate your body mass index\n"
      "so you can know which category you fall into so as to live a healthy live")
print("++++++=========================================++++++")

# get the user weight and  height
print("NB:You should input correct data as required below")
weight = float(input("What is your weight in Kilograms(Kg): "))
height = float(input("What is your height in Meter(m): "))

# calculate the user Body Mass Index from the received data
body_mass_index = floor(weight / (height ** 2))
print(f'Your BMI is {body_mass_index}')

# check which category the user falls in
# underweight < 18.5 
# normal weight 18.5 to 25
# overweight 25 to 30
# obese > 30

if body_mass_index < 18.5:
    print("You are UNDER-WEIGHT. Try to Gain more weight")
elif body_mass_index >= 18.5 and body_mass_index < 25:
    print("Hurray you are in the category of NORMAL-WEIGHT")
elif body_mass_index >= 25 and body_mass_index <= 30:
    print("You are OVER-WEIGHT try to do some workout")
else:
    print("ALERT!!! You are OBESE. You've gat to work on on your weight.")
    
print("\nTHANKS FOR USING OUR BMI PROGRAM")