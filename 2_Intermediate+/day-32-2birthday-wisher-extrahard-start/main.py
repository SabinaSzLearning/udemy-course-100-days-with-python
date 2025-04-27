import smtplib
import datetime as dt
import random
import pandas as pd

my_email = "...@gmail.com"
my_password = "..."

data = pd.read_csv('birthdays.csv')

now = dt.datetime.now()
for i in data.index:

    if now.month == data.month[i] and now.day == data.day[i]:
        number = random.randint(1,3)
        with open(f'letter_templates\letter_{number}.txt', mode='r') as f:
            letter = f.read()
            letter = letter.replace('[NAME]',data.name[i])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email,my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="...@gmail.com",
                msg=f"Subject:Happy B-day!\n\n{letter}"
            )