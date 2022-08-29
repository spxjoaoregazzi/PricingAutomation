from asyncio.windows_events import NULL
from cmath import isnan
import pandas as pd
import numpy as np
import datetime as dt
from bbgApi import get_bond_price, get_cds_data, lastbusyday, addBbgPrice

def testing():
    #isin = "XS2384698994"XS2384698994
    isin = "USN20137AD23"
    date = "2022-08-26"
    result = get_bond_price(isin, date)
    print(result)
    # print(result['value'].get(0))

    ticker = "SPHW06UV"
    #result2 = get_cds_data(ticker, date)
    #print(result2)

testing()

date = str(lastbusyday(dt.date.today()))
''' 
# Opening pricing xlsm
try:
    xls = pd.ExcelFile("P:\RiskTechnology\Pricing\pricing.xlsm")
    bond_sheet = pd.read_excel(xls, 'bond')
    cds_sheet = pd.read_excel(xls, 'cds')
except:
    raise Exception("Pricing xlsm in not properly formatted or is not in the path P:\RiskTechnology\Pricing\pricing.xlsm")

print(bond_sheet[:30])
new_bond_sheet = addBbgPrice(bond_sheet,'Unnamed: 3', date)

'''