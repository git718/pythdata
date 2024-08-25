import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl
import os

data = './data'

dataContents = os.listdir(data)

months2023 = []

for dir in dataContents:
    months2023.append(dir)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

sortedMonths2023 = []

for month in months:
    for month2023 in months2023:
        if month in month2023 or month.lower() in month2023:
            sortedMonths2023.append(month2023)

orderedLinks = []

for month in sortedMonths2023:
    folderContents = os.listdir(data + F"/{month}")
    folderContents.sort()
    for file in folderContents:
        orderedLinks.append(data + f"/{month}/{file}")

allDataFrames = []

for link in orderedLinks:
    df = pd.read_csv(link, dtype={"MEXSTATE": "string", "CONTCODE": "string"})
    allDataFrames.append(df)

oneData = pd.concat(allDataFrames)
# y = []
# x = np.unique(np.array(oneData["MONTH"]))
# for i in x:
#     newdata = oneData.loc[oneData["MONTH"] == i]
#     total = np.sum(np.array(newdata["VALUE"]))
#     y.append(total)
# mpl.xlabel("months")
# mpl.ylabel("value")
# mpl.plot(x, y)
# mpl.show()

# y1 = []
# x1 = np.unique(np.array(oneData["MONTH"]))
# for i in x1:
#     newdata1 = oneData.loc[oneData["MONTH"] == i]
#     total1 = np.sum(np.array(newdata1["SHIPWT"]))
#     y1.append(total1)
# mpl.xlabel("months")
# mpl.ylabel("weight")
# mpl.plot(x1, y1)
# mpl.show()

eight_month = oneData.loc[oneData["MONTH"] == 8]
print(eight_month.mode())

commodities_arr = []
for goods_code in range(0, 99):
    if len(str(goods_code)) < 2:
        goods_code = "0" + str(goods_code)
    else:
        goods_code = str(goods_code)
    commodities_arr.append(goods_code)

print(eight_month)
result = {}
for i in commodities_arr:
    sum = np.sum(np.array(eight_month["SHIPWT"] == i))
    result[i] = sum
