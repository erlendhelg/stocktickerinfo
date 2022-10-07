import requests
import json
import finnhub
import pandas as pd
finnhub_client = finnhub.Client(api_key="cbmhtaqad3i035onbt50")
import pandas
# https://github.com/Finnhub-Stock-API/finnhub-python
# https://finnhub.io/docs/api/

i = 0

#
# df = pd.DataFrame([[10, 20, 30], [100, 200, 300]],
#                   columns=['foo', 'bar', 'baz'])
# def get_methods(object, spacing=20):
#   methodList = []
#   for method_name in dir(finnhub_client):
#     try:
#         if callable(getattr(object, method_name)):
#             methodList.append(str(method_name))
#     except Exception:
#         methodList.append(str(method_name))
#   processFunc = (lambda s: ' '.join(s.split())) or (lambda s: s)
#   for method in methodList:
#     try:
#         print(str(method.ljust(spacing)) + ' ' +
#               processFunc(str(getattr(object, method).__doc__)[0:90]))
#     except Exception:
#         print(method.ljust(spacing) + ' ' + ' getattr() failed')
#
# get_methods(df['foo'])

# test = finnhub_client.quote("AAPL")
# print(pd.DataFrame(test))


test = (dir(finnhub_client))
matches = []
for i in test:
    func = "company_executive"
    if func in i:
        matches.append(i)
        print(matches[0])

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

# Company Peers


ticker = input("Enter the stock ticker: ")
info_type = input("please enter info type: ")
gme = StockInfo(ticker, info_type)

gme.get_info_type()