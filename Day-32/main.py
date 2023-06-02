import pandas
from datetime import datetime
from smtplib import SMTP
from random import randint

data = pandas.read_csv("./birthdays.csv")
data_frame = pandas.DataFrame(data)
users_data = {(user_data["day"], user_data["month"]):(user_data["name"], user_data["email"]) for _, user_data in data_frame.iterrows()}


now = datetime.now()
todays_date = (now.day, now.month)

def checker() -> tuple:
    for dob, details in users_data.items():
        if dob == todays_date:
            return details


if todays_date in users_data:
    print("yes")
    user_details = checker()
    name = user_details[0]
    email = user_details[1]
    letter_path = f"letter_templates/letter_{randint(1, 3)}.txt"
    with open(letter_path, "r") as letter:
        letter_lines = letter.read()
        new_letter = letter_lines.replace("[NAME]", name)
    bot_mail = "ZikTech001@outlook.com"
    bot_password = "ThePyPass"

    with SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(bot_mail, bot_password)
        connection.sendmail(
            from_addr=bot_mail, 
            to_addrs=email, 
            msg=f"Happy Birthday \n\n{new_letter}"
            )
