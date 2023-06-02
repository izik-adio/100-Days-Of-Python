from smtplib import SMTP
from datetime import datetime
from typing import final
from random import choice

EMAIL : final = "ZikTech001@outlook.com"
PASSWORD : final = "ThePyPass"

with open("C:/Users/isaac/Desktop/project/python projects/100-Days-Of-Python/Day-32/quotes.txt", "r") as quotes_db:
    quotes = quotes_db.readlines()

def send_mail():
    quote = choice(quotes)
    print(quote)
    with SMTP(host="smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs="adioisaac24@gmail.com", msg=f"subject: Your Monday Motivation\n\n{quote}")

now = datetime.now()
send_mail()