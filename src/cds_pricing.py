# -*- coding: utf-8 -*-
"""
@author: joao.regazzi
"""

import pandas as pd
import datetime as dt
from database.get_data import addBbgCDSPrice
import config.config as config
from pyrisk import days_ago


def main(date):
    print("\nDATE: "+ str(date))
    # Opening pricing xlsm
    try:
        xls = pd.ExcelFile("P:\RiskTechnology\Pricing\pricing.xlsm")
        cds_sheet = pd.read_excel(xls, 'cds')
    except:
        raise Exception("Pricing xlsm in not properly formatted or is not in the path P:\RiskTechnology\Pricing\pricing.xlsm")

    # Adding the correct cds prices to the sheet
    addBbgCDSPrice(cds_sheet, 'Unnamed: 3', date)
    cds_sheet = cds_sheet.rename(columns={'Unnamed: 1':'Product', 'Unnamed: 5':'Spread', 'Unnamed: 6':'Spread BTG', 'Unnamed: 9':'Cash Settled Amount BTG'}, inplace=True)
    print(cds_sheet)
    print(cds_sheet[['Product', 'Spread', 'Spread BTG', 'Cash Settled Amount BTG', 'bbg spread', 'bbg cash', 'true spread dif', 'true cash dif']])


if __name__ == '__main__':
    pd.options.mode.chained_assignment = None  # default='warn'
    date = days_ago(1)
    main(date)

# ANOTAÇÕES: (fazer futuramente)
# Melhorar verificamento de dif3