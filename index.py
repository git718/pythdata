import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl
import os

# read csv file indo dataframe
df = pd.read_csv("./Border_Crossing_Entry_Data.csv")
#convert object types to string types
df = df.convert_dtypes()
#import array with months to systemize month/year data from the dataframe
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul","Aug", "Sep", "Oct", "Nov", "Dec"]
dates = np.unique(df["Date"])

month_data = []
for i in months:
    arr = []
    for j in dates:
        if i in j:
            arr.append(j)
    month_data.append(arr)

sorted_dates = []
counter = 0
while counter < len(i):
    for i in month_data:
        sorted_dates.append(i[counter])
    counter = counter + 1
