

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

print(df.head())


