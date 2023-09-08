import os
import requests
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def check_stock():
    alphavantage_api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
    alphavantage_endpoint = "https://www.alphavantage.co/query"
    alphavantage_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": alphavantage_api_key
    }

    response = requests.get(url=alphavantage_endpoint, params=alphavantage_params)
    stocks_time_series_dict = response.json()["Time Series (Daily)"]

    stocks_time_series = list(stocks_time_series_dict.keys())

    yesterday_date = stocks_time_series[0]
    day_before_yesterday_date = stocks_time_series[1]

    yesterday_trade = float(stocks_time_series_dict[yesterday_date]["4. close"])
    day_before_yesterday_trade = float(stocks_time_series_dict[day_before_yesterday_date]["4. close"])

    ratio = yesterday_trade / day_before_yesterday_trade
    if ratio >= 1.01:
        ratio = round(ratio - 1, 3) * 100
        return ratio
    elif ratio <= 0.99:
        ratio = round(1 - ratio, 3) * 100
        return -ratio


def get_news(keyword="Tesla"):
    news_api_endpoint = "https://newsapi.org/v2/top-headlines?"
    news_api_params = {
        "q": keyword,
        "apiKey": "2a04e633a74548f3908a2226c414b10d",
        "pageSize": 3,
    }

    news_response = requests.get(url=news_api_endpoint, params=news_api_params)
    news_articles = news_response.json()["articles"]

    return news_articles


def send_message(stock_change_in_percent, news_articles):
    arrow = "up "
    if stock_change_in_percent < 0:
        stock_change = -stock_change_in_percent
        arrow = "down "

    headline = news_articles[0]["title"]
    brief = news_articles[0]["description"]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        my_mail = os.environ.get("MAIL_MAILBLAZER")
        password = "nqkciqmhjoxtphuz"

        text = [f"Subject:TSLA: ", arrow, str(stock_change_in_percent), f"%\n\nHeadline{headline}:\nBrief:{brief}"]
        message = "".join(text)
        # print(message)

        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(to_addrs=my_mail, from_addr=my_mail, msg=message)

        print("mail sent.")


send_message(stock_change_in_percent=check_stock(), news_articles=get_news())

