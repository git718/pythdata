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

df_trucks = df.loc[df["Measure"] == "Trucks"]
# we get information only about trucks crossing border in the period between 1996 and 2023
trucks_data = []
for i in sorted_dates:
    df_monthly_trucks = df_trucks.loc[df_trucks["Date"] == i]
    trucks_per_month = np.sum(np.array(df_monthly_trucks["Value"]))
    trucks_data.append(trucks_per_month)

x = sorted_dates
y = trucks_data
mpl.xlabel("1996 - 2023 yy")
mpl.ylabel("Trucks crossing border")
mpl.plot(x, y)
mpl.show()
# Figure A shows that sudden drops happened in year 2008 (during global economic shock) and in 2020 (approximately April) which could be due to Covid situation.
# Most common ups and downs are due to changing seasons of the year: ups take place at around spring time, downs in December (Christmas time and end of the year)