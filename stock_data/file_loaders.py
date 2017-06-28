import os
from datetime import date
import urllib.request

LOCAL_PATH = "c:/wutemp/data"
SYMBOLS = ['AAPL', 'MSFT']

def load_historical_price(symbols=SYMBOLS, from_dt=date(2001,1,1), to_dt=date(2017,1,1)):
    for sym in symbols:
        localfile = LOCAL_PATH + "/" + sym + ".csv"
        try:
            os.remove(localfile)
        except OSError:
            pass
        urllib.request.urlretrieve("http://www.google.com/finance/historical?q=" + sym + "&startdate=" + from_dt.strftime('%m/%d/%Y') + "&enddate=" + to_dt.strftime('%m/%d/%Y') + "&output=csv", localfile)

#load_historical_price(['AAPL','MSFT'])


