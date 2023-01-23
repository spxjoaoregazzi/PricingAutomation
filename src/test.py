import pandas as pd
from pyrisk import days_ago

import database.get_data as gd
import config.config as config


def test(date, cds, cds_list):

    print(gd.get_cds_data(cds, date))

    print(gd.get_cds_list_price(cds_list, date))


pd.options.mode.chained_assignment = None  # default='warn'

date = days_ago(0)
cds = 'SPKS0ATT CORP'
cds_list = ["SPKS0ATT CORP", "CBRZ1U5 CORP"]

print(f"DATE: {date}")

test(date, cds, cds_list)
