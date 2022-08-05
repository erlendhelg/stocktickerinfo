import requests
import json
import finnhub
finnhub_client = finnhub.Client(api_key="cbmhtaqad3i035onbt50")

# https://github.com/Finnhub-Stock-API/finnhub-python
# https://finnhub.io/docs/api/

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
bitcoinprice = requests.get(url)

print("Price of Bitcoin is: " + "\n" + "€" + bitcoinprice.json()["bpi"]["EUR"]["rate"])

# Stock candles
print(finnhub_client.company_basic_financials('AAPL', 'all'))
