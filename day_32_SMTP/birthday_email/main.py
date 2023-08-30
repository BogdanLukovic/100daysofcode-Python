# #################### Extra Hard Starting Project ##################### #

import datetime
import smtplib
import random
import pandas
from os import listdir


def get_birthday_list():
    data = pandas.read_csv("birthdays.csv")
    birthdays_dict = data.to_dict()

    months = list((birthdays_dict["month"].values()))
    days = list(birthdays_dict["day"].values())
    emails = list(birthdays_dict["email"].values())
    names = list(birthdays_dict["name"].values())

    birthday_list = [(names[i], emails[i], months[i], days[i]) for i in range(len(months))]

    return birthday_list


def get_letter(person):
    random_letter_file_name = random.choice(listdir("letter_templates"))

    with open(f"letter_templates/{random_letter_file_name}") as file:
        person_name = person[0]
        letter = file.read().replace("[NAME]", person_name).replace("Angela", "Bogdan")
        return letter


def send_letter(person, letter):
    my_email = 'mailblazer420@gmail.com'
    password = "jpdpnklvroznjwip"

    recipient_email = person[1]

    letter_with_subject = f"Subject:Happy birthday! \n\n{letter}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=letter_with_subject)

    print("Birthday letter send!")


def check_birthdays():
    birthday_list = get_birthday_list()

    now = datetime.datetime.now()
    today = tuple((now.month, now.day))

    for person in birthday_list:
        birthday = (person[2], person[3])
        if birthday == today:
            letter = get_letter(person)
            send_letter(person, letter)


check_birthdays()
