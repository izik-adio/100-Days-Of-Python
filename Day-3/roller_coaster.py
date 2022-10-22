# this program checks if a user is fit to purchase a roller coaster and if yes tells the user the price

height = int(input("Kindly input your height in cm: "))
if height > 120:
    print("Okay you can ride")
    age = int(input("How old are you: "))
       
    def pics(bill):
        picture = True 
        while picture:
            pics = input("Do you want photos? ")
            yes = ["yes", "YES", "Yes", "Y", "y"]
            no = ["no", "NO", "No", "N", "n"]
            if pics in yes:
                bill = bill + 3
                return bill
                picture = False
            elif pics in no:
                picture = False
                return bill               
            else:
                print("Invalid input")
    if age < 12:
        bill = pics(5)
        print(f"Your bill is {bill}")
    elif age >= 12 and age < 18:
        bill = pics(7)
        print(f"your bill is {bill}")
    elif age >= 18:
        bill = pics(12)
        print(f"your bill is {bill}")
        
else:
    print("Sorry you cant ride. Try to grow taller")