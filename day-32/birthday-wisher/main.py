import smtplib
from datetime import datetime
import pandas
import random

MY_EMAIL = "ahmed.alwardani.1995@gmail.com"
PASSWORD = "yrzafyvxammkdtkk"
GMAIL_HOST = "smtp.gmail.com"

today_tuple = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(GMAIL_HOST) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject: Happy birthday!!!\n\n{content}")