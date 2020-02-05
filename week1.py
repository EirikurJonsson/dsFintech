

import pandas as pd
try:
    df = pd.read_csv("ETH_EUR.csv", parse_dates = ["Date"])
    df2 = pd.read_csv(("NASDAQOMX.csv"))
except FileNotFoundError:
    import quandl
    df = quandl.get("GDAX/ETH_EUR", authtoken = "3CdfXCg8D_CWBs7UAwKr")
    df2 = quandl.get("NASDAQOMX/OMXN40", authtoken= "3CdfXCg8D_CWBs7UAwKr")
    df.to_csv("ETH_EUR", encoding = "utf-8")
    df2.to_csv("NASDAQOMX", encoding = "utf-8")

# print(df.head())
# print("=====================================================")
# print(df2.head())

def nDescriptive(df, year):
    '''
    Making a function that prints some descriptive numbers
    for each column. 
    TODO: I still havent gotten it to work for each year, meaning I want
    to be able to select a specific year. 
    '''
    import itertools
    nList = list(df.columns.values)
    if year > 0:
        for i in nList:
            print("======================================================")
            print(f"The Mean: {df[i].loc(df.index == year).mean()}")
            print(f"The Median: {df[i].loc(df.index == year).median()}")
            print(f"The Std: {df[i].loc(df.index == year).std()}")
            print(f"The quantile: {df[i].loc(df.index == year).quantile([0.25,0.5,0.75])}")
        


nDescriptive(df, 2010)
