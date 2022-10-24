# this is a program that check if a year is leap year or not

# accept user input
from pickletools import int4


print("~~~~~~~~~~~~ Leap Year Checker ~~~~~~~~~~~~")
check = True
while check:
    try:
        year = int(input("Input the year you'll like to check: "))
        year = str(year)
        if len(year) == 4:
            year = int(year)
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print(f"{year} is a leap year")
                    else:
                        print(f"{year} is not a leap year")
                else:
                    print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
            opt = input("Would you like to check other years: ")
            yes = ["yes", "YES", "Yes", "Y", "y"]
            no = ["no", "NO", "No", "N", "n"]
            if opt in yes:
                check = True
            elif opt in no:
                check = False
            else:
                break

        else:
            print("Input a valid year eg: 2022 ")
            check = True
    except ValueError:
        print("You should input only numbers")
        check = True
