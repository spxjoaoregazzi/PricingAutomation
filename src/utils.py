# -*- coding: utf-8 -*-
"""
@author: joao.regazzi
"""

import pandas as pd
import datetime as dt

def analyseBondsDif(bond_df):
    # Create deepcopy of the original 
    bond_df = bond_df.copy(deep=True)
    bond_df.drop(bond_df.index[[0,5]])
    analyse_list = []

    for i, dif in enumerate(bond_df["real dif"]):
        # If Product not blank and ISIN blank
        product = bond_df["Unnamed: 1"].get(i)
        isin = bond_df["Unnamed: 3"].get(i)
        if (not pd.isnull(product)) and (pd.isnull(isin)) and product != "Precificação - Bond":
            analyse_list.append(bond_df["Unnamed: 1"].get(i))
        # If difference is not blank and is greater than 0.5
        if not pd.isnull(dif):
            if float(dif) > 0.1:
                analyse_list.append(bond_df["Unnamed: 1"].get(i))
    if analyse_list:
        print(f"\nNeed to verify the following bonds:")
        for bond in analyse_list:
            print(bond)
    else:
        print("\nAll bonds are ok!")
    return analyse_list



def analyseDif3(bond_df):
    # Create deepcopy of the original 
    bond_df = bond_df.copy(deep=True)
    bond_df.drop(bond_df.index[[0,5]])
    analyse_list = []

    for i, dif3 in enumerate(bond_df['Unnamed: 11']):
        if (not (pd.isnull(dif3) or pd.isnull(bond_df['Unnamed: 17'].get(i)))) and dif3 != "Dif 3":
            if float(dif3) != 0 and float(bond_df['Unnamed: 17'].get(i)) == 1:
                analyse_list.append(bond_df['Unnamed: 1'].get(i))
    
    if analyse_list:
        print(f"\nNeed to verify the dif3 for the following bonds:")
        for bond in analyse_list:
            print(bond)
    else:
        print('\nAll dif3 are correct')
    return analyse_list


def analyse_cds_dif(cds_df):
    # Create deepcopy of the original 
    cds_df = cds_df.copy(deep=True)
    cds_df.drop(cds_df.index[[0,5]])
    analyse_list = []

    for i, dif in enumerate(cds_df["real dif"]):
        # If Product not blank and ISIN blank
        product = cds_df["Unnamed: 1"].get(i)
        isin = cds_df["Unnamed: 3"].get(i)
        if (not pd.isnull(product)) and (pd.isnull(isin)) and product != "Precificação - Bond":
            analyse_list.append(cds_df["Unnamed: 1"].get(i))
        # If difference is not blank and is greater than 0.5
        if not pd.isnull(dif):
            if float(dif) > 0.1:
                analyse_list.append(cds_df["Unnamed: 1"].get(i))
    if analyse_list:
        print(f"\nNeed to verify the following bonds:")
        for bond in analyse_list:
            print(bond)
    else:
        print("\nAll bonds are ok!")
    return analyse_list