# -*- coding: utf-8 -*-
"""
@author: joao.regazzi
"""

import pandas as pd
import numpy as np
import requests
import config.config as config
import database.queries.data_source as data_source


def get_bond_price(isin, date):

    date = str(date)

    url = data_source.Source().bdh_120
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


def get_bond_list_price(isin_list, date):

    date = str(date)
    
    bval_list = [isin+'@BVAL CORP' for isin in isin_list]

    url = data_source.Source().bdh_120
    req = requests.post(url, auth=(config.username, config.password), json={
    "tickers": [
        bval_list
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


def get_cds_data(ticker, date):

    date = str(date)

    url = data_source.Source().ref_hist_120
    req = requests.post(url, auth=(config.username, config.password), json={
    "tickers": [
        f"{ticker}"
    ],
    "flds": [
        "CDS_CASH_SETTLED_AMOUNT",
        "CDS_FLAT_SPREAD",
        "CDS_REPL"
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
    

def get_cds_list_price(ticker_list, date):

    date = str(date)

    url = data_source.Source().ref_hist_120
    req = requests.post(url, auth=(config.username, config.password), json={
    "tickers": ticker_list,
    "flds": [
        "CDS_CASH_SETTLED_AMOUNT",
        "CDS_FLAT_SPREAD",
        "CDS_REPL"
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
