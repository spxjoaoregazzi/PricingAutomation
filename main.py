# -*- coding: utf-8 -*-
"""
@author: joao.regazzi
"""

import pandas as pd
import datetime as dt
from database.bbgApi import addBbgBondPrice, addBbgCDSPrice
from utils import analyseBondsDif, analyseDif3
import config.config as config


def main(date):
    print("\nDATE: "+date)
    # Opening pricing xlsm
    try:
        xls = pd.ExcelFile("P:\RiskTechnology\Pricing\pricing.xlsm")
        bond_sheet = pd.read_excel(xls, 'bond')
        # cds_sheet = pd.read_excel(xls, 'cds')
        # print(cds_sheet)
    except:
        raise Exception("Pricing xlsm in not properly formatted or is not in the path P:\RiskTechnology\Pricing\pricing.xlsm")

    # Adding the correct bond prices to the sheet
    addBbgBondPrice(bond_sheet,'Unnamed: 3', date)

    # Analysing the results
    analyseBondsDif(bond_sheet)
    analyseDif3(bond_sheet)

    # Adding the correct cds prices to the sheet
    # addBbgCDSPrice(cds_sheet, 'Unnamed: 3', date)



if __name__ == '__main__':
    pd.options.mode.chained_assignment = None  # default='warn'
    date = config.date
    main(date)

# ANOTAÇÕES: (fazer futuramente)
# Melhorar verificamento de dif3
# Fazer não ser possível selecionar data como feriado