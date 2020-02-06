

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
try:
    df = pd.read_csv("ETH_EUR.csv", parse_dates = ["Date"])
    df2 = pd.read_csv(("NASDAQOMX.csv"))
except FileNotFoundError:
    import quandl
    df = quandl.get("GDAX/ETH_EUR", authtoken = "3CdfXCg8D_CWBs7UAwKr")
    df2 = quandl.get("NASDAQOMX/OMXN40", authtoken= "3CdfXCg8D_CWBs7UAwKr")
    df.to_csv("ETH_EUR", encoding = "utf-8")
    df2.to_csv("NASDAQOMX", encoding = "utf-8")

'''
Joining the data frame using the join function of pandas
data frame. Will be using the date time index to join
by.
'''
##########################################################################
############# Not neccissary not run the next two lines###################
#############    unless you dont have this csv file    ###################
########################################################################## 
# df3 = df.join(df2, lsuffix = "_ETH_EUR", rsuffix = "_OMX")
# df3.to_csv("joined.csv")

df3 = pd.read_csv("joined.csv")
df3 = df3.set_index("Date")

def nDescriptive(df, year = 0):
    '''
    Making a function that prints some descriptive numbers
    for each column. Can print for all the years or one specific year. 
    '''
    nList = list(df.columns.values)
    df["years"] = pd.DatetimeIndex(df.index).year

    if year > 0:
        for i in nList[:-1]:
            print("======================================================")
            print("Total per",year, "for ",i)
            print(f"The Mean: {df[i].loc[df.years == year].mean()}")
            print(f"The Median: {df[i].loc[df.years == year].median()}")
            print(f"The Std: {df[i].loc[df.years == year].std()}")
            print(f"The quantile: {df[i].loc[df.years == year].quantile([0.25,0.5,0.75])}")
    elif year == 0:
        print("Total for all years in the dataset.")
        for i in nList[:-1]:
            print("======================================================")
            print(i)
            print(f"The Mean: {df[i].mean()}")
            print(f"The Median: {df[i].median()}")
            print(f"The Std: {df[i].std()}")
            print(f"The quantile: {df[i].quantile([0.25,0.5,0.75])}")
        

def nVis(df, y, roll):
    if isinstance(roll, list):
        plt.figure(figsize = (16,5), dpi = 100)
        plt.plot(df.index, df[y], color = "tab:red", label = y)
        plt.gca().set(title = "Moving averages", xlabel = "Date", ylabel = y)
        for i in (roll):
            df[f"ma{i}"] = df[y].rolling(window = i, min_periods = 0).mean()
            plt.plot(df.index, df[f"ma{i}"], label = df[f"ma{i}"].name)
    else:
        df[f"ma{roll}"] = df[y].rolling(window = roll, min_periods = 0).mean()
        plt.figure(figsize = (16,5), dpi = 100)
        plt.plot(df.index, df[f"ma{roll}"], label = df[f"ma{roll}"].name)
        plt.plot(df.index, df[y], color = "tab:red", label = y)
        plt.gca().set(title = "Moving averages", xlabel = "Date", ylabel = y)
    plt.legend()
    plt.show()


def nLogReturns(df, x):
    '''
    This function takes a data frame and the column
    that is to be used to calculate log returns. 
    For this function I will not add a time seperator since
    it is not neccissary in this case.
    '''
    df["pctChange"] = df[x].pct_change()
    df["log_ret"] = np.log(df[x]) - np.log(df[x].shift(1))
    nList = ["pctChange", "log_ret"]
    for i in nList:
        print("Mean:", df[i])
        print("Median", df[i])
        print("Std:", df[i])
        plt.hist(df[i], label = i, bins = 40)
        print("========================================================")
    plt.gca().set(title = f"Log return of {x}", xlabel = "Date")
    plt.legend()
    plt.show()

