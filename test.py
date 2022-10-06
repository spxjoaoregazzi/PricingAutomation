import database.bbgApi as api

ticker = 'SPHW06UV'
date = '2022-09-16'
print(api.get_cds_data(ticker, date))

cds_list = [(1, "SPHW06UV CORP"), (2, "CCHIL1U5 CORP"), (3, "CFM1U5 CORP")]
# cds_list = [(1, "SPHW06UV CORP")]
print(api.get_cds_ListPrice(cds_list, date))