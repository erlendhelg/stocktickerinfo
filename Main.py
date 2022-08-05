import requests
import json


url = "https://api.coindesk.com/v1/bpi/currentprice.json"
bitcoinprice = requests.get(url)

print("Price of Bitcoin is: " + "\n" + "€" + bitcoinprice.json()["bpi"]["EUR"]["rate"])
