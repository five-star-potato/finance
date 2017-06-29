import os
from datetime import date
import urllib.request
import pandas as pd

LOCAL_PATH = "c:/wutemp/data"
PRICE_SUFFIX = "_price.csv"
RATIOS_SUFFIX = "_ratios.csv"

SYMBOLS = ['AAPL', 'MSFT']

def load_historical_price(symbols=SYMBOLS, from_dt=date(2001,1,1), to_dt=date(2017,1,1)):
    for sym in symbols:
        localfile = LOCAL_PATH + "/" + sym + PRICE_SUFFIX
        try:
            os.remove(localfile)
        except OSError:
            pass
        urllib.request.urlretrieve("http://www.google.com/finance/historical?q=" + sym + "&startdate=" + from_dt.strftime('%m/%d/%Y') + "&enddate=" + to_dt.strftime('%m/%d/%Y') + "&output=csv", localfile)

def load_ratios(symbols=SYMBOLS):
    for sym in symbols:
        localfile = LOCAL_PATH + "/" + sym + RATIOS_SUFFIX
        try:
            os.remove(localfile)
        except OSError:
            pass
        urllib.request.urlretrieve("http://financials.morningstar.com/ajax/exportKR2CSV.html?t=" + sym, localfile)

def read_price_csv(sym):
    localfile = LOCAL_PATH + "/" + sym + PRICE_SUFFIX
    csv = pd.read_csv(localfile, delimiter=",", index_col="Date")
    return csv

def read_ratios_csv(sym):
    localfile = LOCAL_PATH + "/" + sym + RATIOS_SUFFIX
    csv = pd.read_csv(localfile, delimiter=",")
    return csv
#load_historical_price(['AAPL','MSFT'])


