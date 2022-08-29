import pandas as pd
import numpy as np
import requests

#ID: PR092
#Mnemonic: PRICING_SOURCE
def get_bond_price(isin, date):
    url = "http://192.168.1.211:3000/bdh"
    req = requests.post(url, auth=('spxrisk', 'risk@1234'), json={
    "tickers": [
        f"{isin}@BVAL CORP"
    ],
    "flds": [
        "PX_LAST"
    ],
    "start_date": date,
    "end_date": date
    })
    print('print(req.json)')
    if req.status_code == 200:
        print("\nConexão com a API realizada com sucesso")
        df = pd.DataFrame(req.json())
        return df
    else:
        return req.status_code


# FLDS: CDS_CASH_SETTLED_AMOUNT CDS_FLAT_SPREAD
def get_cds_data(ticker, date):
    url = "http://192.168.1.211:3000/ref_hist"
    req = requests.post(url, auth=('spxrisk', 'risk@1234'), json={
    "tickers": [
        f"{ticker} CMAN CORP"
    ],
    "flds": [
        "CDS_CASH_SETTLED_AMOUNT",
        "CDS_FLAT_SPREAD"
    ],
    "dates": [
        date
    ],
    "ovrds": {
        }
    })
    if req.status_code == 200:
        print("\nConexão com a API realizada com sucesso")
        df = pd.DataFrame(req.json())
        return df
    else:
        return req.status_code


def addBbgPrice(df, col, date):
    for i in df.index:
        val = df[col].iloc[i]
        if pd.isnull(val) or val == "ISIN":
            df["bbg price"] = np.nan
        else:
            result = get_bond_price(val, date)
            price = str(result['value'].get(0))
            df["bbg price"].iloc[i] = price
            print(f"Price for {val} is {price}" )
    return df


import datetime as dt
def lastbusyday(day):
    lastBusDay = day
    if dt.date.weekday(day) == 0: #if it's Monday
        lastBusDay = lastBusDay - dt.timedelta(days = 3) #then make it Friday
    elif dt.date.weekday(day) == 6: #if it's Sunday
        lastBusDay = lastBusDay - dt.timedelta(days = 2) #then make it Friday
    elif dt.date.weekday(day) == 5: #if it's Saturday
        lastBusDay = lastBusDay - dt.timedelta(days = 1) #then make it Friday
    else:
        lastBusDay = lastBusDay - dt.timedelta(days = 1)
    return lastBusDay