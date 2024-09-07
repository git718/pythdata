import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl
import os

# read csv file into dataframe
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

df_trucks = df.loc[(df["Measure"] == "Trucks") | (df["Measure"] == "Truck Containers Loaded") | (df["Measure"] == "Truck Containers Empty")]
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
# Figure_1 shows that sudden drops happened in year 2008 (during global economic shock) and in 2020 (approximately April) which could be due to Covid situation.
# Most ups and downs are due to changing seasons of the year: ups take place at around spring time, downs in December (Christmas time and end of the year)
#Figure_2 considers not only measure "Trucks", but also adds "Truck Containers Loaded" and "Truck Containers Empty" to the equation. 


#get port names, states, types of vehicles/measures (unique values)

port_names = pd.unique(pd.Series(df["Port Name"].sort_values()))
with open ("./port_names.txt", "w") as f:
    f.write("")
    for i in port_names:
        f.write(i + '\n')

states = pd.unique(pd.Series(df["State"].sort_values()))
with open ("./states.txt", "w") as f:
    f.write("")
    for i in states:
        f.write(i + '\n')

measures = pd.unique(pd.Series(df["Measure"].sort_values()))
with open ("./measures.txt", "w") as f:
    f.write("")
    for i in measures:
        f.write(i + '\n')

