import smtplib
import datetime as dt
from random import choice

my_email = "deddia.programmer@gmail.com"
my_password = ""

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 5:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        quote = choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="deddiapermana97@gmail.com",
                            msg=f"Subject:Motivation of the first day of week\n\n{quote}")
