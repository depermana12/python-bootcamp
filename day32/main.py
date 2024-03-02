import datetime as dt
import pandas as pd
from random import randint
import smtplib

now = dt.datetime.now()
today = (now.month, now.day)

my_email = "deddia.programmer@gmail.com"
my_password = ""

raw_data = pd.read_csv("birthdays.csv")
data_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in raw_data.iterrows()}

if today in data_dict:
    person_birthday = data_dict[today]
    random_template = f"templates/letter_{randint(1, 3)}.txt"
    with open(random_template) as letter:
        contents = letter.read()
        contents_name_replaced = contents.replace("[NAME]", person_birthday["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=person_birthday["email"],
                            msg=f"Subject:HBD {person_birthday["name"]}\n\n{contents_name_replaced}")
