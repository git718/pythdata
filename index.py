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
