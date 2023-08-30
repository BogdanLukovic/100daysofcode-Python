import random
import smtplib
import datetime as dt

now = dt.datetime.now()

if now.weekday() == 2:
    with open("quotes.txt", 'r') as file:
        text = file.read()
        quotes = text.split("\n")

    quote_of_day = random.choice(quotes)

    message = "Subject:Hello\n\n" + quote_of_day

    my_email = 'mailblazer420@gmail.com'
    password = "jpdpnklvroznjwip"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=message)

    print("mail sent")
