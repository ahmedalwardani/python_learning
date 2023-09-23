import requests
from bs4 import BeautifulSoup
import lxml
import smtplib


IPHONE_CASE_URL = ("https://www.amazon.ca/TAURI-iPhone-15-Pro-Protection/dp/B0CBBKM879/ref=sr_1_6?keywords=iphone+15"
                   "+pro+case&qid=1695469065&sr=8-6")

FROM_EMAIL = "ahmed.alwardani.1995@gmail.com"
PASSWORD = "yrzafyvxammkdtkk"
GMAIL_HOST = "smtp.gmail.com"
TO_EMAIL = "aalwa049@gmail.com"
BUY_PRICE = 20

request_headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/116.0.0.0 Safari/537.36"
}

response = requests.get(IPHONE_CASE_URL, headers=request_headers)
response.raise_for_status()

soup = BeautifulSoup(response.content, "lxml")

price_with_currency = soup.find(class_="a-offscreen").getText()
price = float(price_with_currency.split("$")[1])
title = soup.find(id="productTitle").getText().strip()

if price < BUY_PRICE:
    message = f"{title} is now {price}"
    with smtplib.SMTP(GMAIL_HOST, port=587) as connection:
        connection.starttls()
        connection.login(FROM_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{IPHONE_CASE_URL}".encode("utf-8")
        )
