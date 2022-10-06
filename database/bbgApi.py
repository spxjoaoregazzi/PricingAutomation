# -*- coding: utf-8 -*-
"""
@author: joao.regazzi
"""

import pandas as pd
import numpy as np
import requests
import config.config as config
import database.queries.data_source as data_source

#ID: PR092
#Mnemonic: PRICING_SOURCE
def get_bond_price(isin, date):
    url = data_source.Source().bond_endpoint
    req = requests.post(url, auth=(config.username, config.password), json={
    "tickers": [
        f"{isin}@BVAL CORP"
    ],
    "flds": [
        "PX_LAST"
    ],
    "start_date": date,
    "end_date": date
    })
    if req.status_code == 200:
        print("\nConexão com a API realizada com sucesso")
        df = pd.DataFrame(req.json())
        return df
    else:
        return req.status_code


def get_bondlist_price(bondlist, date):
    list_isin = [tuple[1] for tuple in bondlist]
    # for isin in list_isin: isin += "@BVAL CORP"
    url = data_source.Source().bond_endpoint
    req = requests.post(url, auth=(config.username, config.password), json={
    "tickers": list_isin,
    "flds": [
        "PX_LAST"
    ],
    "start_date": date,
    "end_date": date
    })
    if req.status_code == 200:
        print("\nConexão com a API realizada com sucesso")
        df = pd.DataFrame(req.json())
        return df
    else:
        return req.status_code


def addBbgBondPrice(bond_sheet, col, date):
    # Get the price of all bonds in the xls, in only one API request
    bond_list = []
    for i in bond_sheet.index:
        val = bond_sheet[col].iloc[i]
        if not (pd.isnull(val) or val == "ISIN"):
            bond_list.append((i, val+"@BVAL CORP"))
    result = get_bondlist_price(bond_list, date)

    # Create new bond_sheet with correct bbg price column in the end
    bond_sheet["bbg price"] = np.nan
    bond_sheet["real dif"] = np.nan
    for tuple in bond_list:
        real_index, isin = tuple[0], tuple[1]
        bbg_index = result[result["ticker"] == isin].index.values[0]
        price = result[result["ticker"] == isin]["value"].get(bbg_index)
        bond_sheet["bbg price"].iloc[real_index] = price # Instert the price in the correct row
        bond_sheet["real dif"].iloc[real_index] = float(price) - float(bond_sheet["Unnamed: 5"].iloc[real_index])
    return bond_sheet


# FLDS: CDS_CASH_SETTLED_AMOUNT CDS_FLAT_SPREAD
def get_cds_data(ticker, date):
    url = data_source.Source().cds_endpoint
    req = requests.post(url, auth=(config.username, config.password), json={
    "tickers": [
        f"{ticker} CORP"
    ],
    "flds": [
        "CDS_CASH_SETTLED_AMOUNT",
        "CDS_FLAT_SPREAD"
    ],
    "dates": [
        date
    ],
    "ovrds": {
       # "Pricing_Source": "CMAN MID"
        }
    })
    if req.status_code == 200:
        print("\nConexão com a API realizada com sucesso")
        df = pd.DataFrame(req.json())
        return df
    else:
        return req.status_code
    

def get_cds_ListPrice(cds_list, date):
    list_ticker = [tuple[1] for tuple in cds_list]
    url = data_source.Source().cds_endpoint
    req = requests.post(url, auth=(config.username, config.password), json={
    "tickers": list_ticker,
    "flds": [
        "CDS_CASH_SETTLED_AMOUNT",
        "CDS_FLAT_SPREAD"
    ],
    "dates": [
        date
    ],
    "ovrds": {
       # "Pricing_Source": "CMAN MID"
        }
    })
    if req.status_code == 200:
        print("\nConexão com a API realizada com sucesso")
        df = pd.DataFrame(req.json())
        return df
    else:
        return req.status_code


def addBbgCDSPrice(cds_sheet, col, date):
    # Get the price of all bonds in the xls, in only one API request
    cds_list = []
    for i in cds_sheet.index:
        val = cds_sheet[col].iloc[i]
        if not (pd.isnull(val) or val == "Ticker BBG"):
            cds_list.append((i, val))
    result = get_cds_ListPrice(cds_list, date)

    # Create new bond_sheet with correct bbg price column in the end
    cds_sheet["bbg spread"] = np.nan
    cds_sheet["bbg cash"] = np.nan
    cds_sheet["real dif spread"] = np.nan
    cds_sheet["real dif cash"] = np.nan
    for tuple in cds_list:
        real_index, ticker = tuple[0], tuple[1]
        bbg_spread_index = result[result["ticker"] == ticker][result["field"] == "CDS_FLAT_SPREAD"].index.values[0]
        bbg_cash_index = result[result["ticker"] == ticker][result["field"] == "CDS_CASH_SETTLED_AMOUNT"].index.values[0]
        spread = result[result["ticker"] == ticker][result["field"] == "CDS_FLAT_SPREAD"]["value"].get(bbg_spread_index)
        cash = result[result["ticker"] == ticker][result["field"] == "CDS_CASH_SETTLED_AMOUNT"]["value"].get(bbg_cash_index)
        print(result["ticker"], spread, cash)
        cds_sheet["bbg spread"].iloc[real_index] = spread # Instert the price in the correct row
        cds_sheet["bbg cash"].iloc[real_index] = cash # Instert the price in the correct row
        cds_sheet["real dif spread"].iloc[real_index] = float(spread) - float(cds_sheet["Unnamed: 5"].iloc[real_index])
        
        cds_sheet["real dif cash"].iloc[real_index] = float(cash) - float(cds_sheet["Unnamed: 9"].iloc[real_index])
    return cds_sheet
