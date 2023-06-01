##################### Extra Hard Starting Project ######################
import pandas
from smtplib import SMTP
from random import choice
from datetime import datetime

# 1. Update the birthdays.csv
data = pandas.read_csv("./birthdays.csv")
processed_data = pandas.DataFrame(data=data)
if 

# 2. Check if today matches a birthday in the birthdays.csv
for n in processed_data:
        print(n)


current_month = datetime.now().month
current_day = datetime.now().day


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

