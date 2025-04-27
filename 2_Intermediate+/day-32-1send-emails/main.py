import smtplib
import datetime as dt
import random

my_email = "...@gmail.com"
my_password = "..."


now = dt.datetime.now()
if now.weekday() == 0:  # if it is monday
    with open('quotes.txt', mode='r') as f:
        quotes = f.readlines()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="...@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{random.choice(quotes)}"
        )