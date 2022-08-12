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



print(finnhub_client.company_news('AAPL', _from="2021-06-01", to="2022-06-10"))

# Company Peers

