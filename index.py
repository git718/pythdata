import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl
import os

df = pd.read_csv("./Border_Crossing_Entry_Data.csv")
df = df.convert_dtypes()
print(df)