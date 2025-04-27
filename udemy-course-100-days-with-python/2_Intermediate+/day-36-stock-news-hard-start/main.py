import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_STOCK = "78B6HMAT55ZCT3YU"
API_KEY_NEWS = '86f7a029deba4b1fbf30f12115ec9e13'

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.


params_stock = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': API_KEY_STOCK
}
response = requests.get(url=STOCK_ENDPOINT, params=params_stock)
response.raise_for_status()
data = response.json()

last_date = data['Meta Data']['3. Last Refreshed']

second_last_day =  datetime.strptime(last_date, "%Y-%m-%d") - timedelta(days=1)
second_last_day = second_last_day.strftime("%Y-%m-%d")

prize1 = data['Time Series (Daily)'][second_last_day]['4. close']
prize2 = data['Time Series (Daily)'][last_date]['4. close']

if abs(float(prize1) - float(prize2))/float(prize2) >= 0.001:

    params_news = {
        'q': COMPANY_NAME,
        'searchIn': 'title',
        'apiKey': API_KEY_NEWS
    }
    response = requests.get(url=NEWS_ENDPOINT, params=params_news)
    response.raise_for_status()
    data = response.json()
    for art in data['articles'][:3]:
        print(art['title'])









#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

