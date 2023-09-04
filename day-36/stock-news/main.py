import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

STOCK_ENDPOINT_API_KEY = "UBLBXLG3Y8RLTDR0"
NEWS_ENDPOINT_API_KEY = "ee0bba511310494990c394f50d697b31"

TWILIO_ACCOUNT_SID = "ACf7dca9c6d5e0a4fb61d80fec0bae5413"
TWILIO_AUTH_TOKEN = "7ac56e8c3565a85dece55b837a4719d9"


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_ENDPOINT_API_KEY
}

stock_endpoint_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_endpoint_response.raise_for_status()
daily_data = stock_endpoint_response.json()["Time Series (Daily)"]
daily_stock_prices = [daily_stock_data for (date, daily_stock_data) in daily_data.items()]

yesterdays_closing_stock_price = float(daily_stock_prices[0]["4. close"])
day_before_yesterdays_closing_stock_price = float(daily_stock_prices[1]["4. close"])

difference = yesterdays_closing_stock_price - day_before_yesterdays_closing_stock_price
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_difference = round((difference / yesterdays_closing_stock_price) * 100)

if abs(percentage_difference) > 1:
    news_parameters = {
        "apiKey": NEWS_ENDPOINT_API_KEY,
        "q": COMPANY_NAME,
        "searchIn": "title"
    }
    news_endpoint_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_endpoint_response.raise_for_status()
    three_most_recent_news_articles = news_endpoint_response.json()["articles"][:3]

    three_most_recent_news_articles_headline_and_description = [f" {STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in
                                                                three_most_recent_news_articles]
    for article in three_most_recent_news_articles_headline_and_description:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=article,
            from_='+19285648193',
            to='+16138525167'
        )
        print(message.status)

