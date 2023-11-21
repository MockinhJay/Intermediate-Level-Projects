import requests
from twilio.rest import Client

STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = "ACbe3ad02ae549e16f982efbce5903f490"
TWILIO_AUTH_TOKEN = "4e59708c68af5470f9b28cde2848d71d"

STOCK_API_KEY = "ZDEHVLG1R8RS21EQ"
NEWS_API_KEY = "c771bd0fa64443979548e0a0e49e409b"

# stock_params = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": COMPANY_NAME,
#     "apikey": STOCK_API_KEY,
# }

response = requests.get(
    f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey=ZDEHVLG1R8RS21EQ')
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_data_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_data_closing_price)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "🔻"


diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

if abs(diff_percent) > 2:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    print(articles)

    three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadlineL: {articles['title']}. \nBreif: {articles['description']}" for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+19378775799",
            to="+16393843665"

        )