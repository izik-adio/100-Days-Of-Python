from smtplib import SMTP
from datetime import datetime
from typing import final
from random import choice

EMAIL : final = "ZikTech001@outlook.com"
PASSWORD : final = "ThePyPass"
TODAY : final = 0

with open("./quotes.txt", "r") as quotes_db:
    quotes = quotes_db.readlines()

def send_mail():
    quote = choice(quotes)
    print(quote)
    with SMTP(host="smtp-mail.outlook.com", port=587) as connection:
        print("created connection")
        connection.starttls()
        print("started tls")
        connection.login(username=EMAIL, password=PASSWORD)
        print("logged in")
        connection.sendmail(from_addr=EMAIL, to_addrs="adioisaac24@gmail.com", msg=f"subject: Your Monday Motivation\n\n{quote}")
        print("sent")

now = datetime.now()

if now.weekday() == TODAY:
    send_mail()
