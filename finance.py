import yfinance as yf
from datetime import datetime, timedelta

today = datetime.today()
START_STR = today.strftime('%Y-%m-%d')

d = today - timedelta(days=100)
OTHER_STR = d.strftime('%Y-%m-%d')


def get_raw_dataframe_all(symbol="^GSPC", dateRng="max"):
    # Other time options include: "10y", "5y", "1mo", etc.
    ticker = yf.Ticker(symbol)
    raw = ticker.history(period=dateRng).Close
    return(raw)


def get_raw_dataframe_daterange(symbol="^GSPC", start="", end=""):
    ticker = yf.Ticker(symbol)
    raw = ticker.history(period="max")
    return raw
