import requests
import json
import finnhub
import pandas as pd
finnhub_client = finnhub.Client(api_key="cbmhtaqad3i035onbt50")

# https://github.com/Finnhub-Stock-API/finnhub-python
# https://finnhub.io/docs/api/

class StockInfo:

    def __init__(self, ticker, inf_type):
        self.ticker = ticker.upper()
        self.inf_type = inf_type

    def get_info_type(self):
        functions = (dir(finnhub_client))
        matches = []
        for i in functions:
            if self.inf_type in i:
                matches.append(i)
        if len(matches) > 1:
            print("please select from list: " + matches)
        else:
            try:
                print(getattr(finnhub_client, matches[0])(self.ticker))
            except TypeError:
                range1 = input("Please enter from range (YYYY-MM-DD): ")
                range2 = input("Please enter to range (YYYY-MM-DD): ")

                res = getattr(finnhub_client, matches[0])(self.ticker, _from=range1, to=range2)
                print(res)


gme = StockInfo('"AAPL"', "company_news")

gme.get_info_type()
