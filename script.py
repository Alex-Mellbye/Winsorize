
# "conda install -c conda-forge pyreadstat"

import pandas as pd
from scipy.stats.mstats import winsorize

df = pd.read_spss(r'C:\Users\alex_\Documents\Anne Trana\Analysefil_BPD_Winsorizing.sav')

print(df.columns)
print(df.isnull().sum())

print(max(df["NSSI_lifetime"]))
print(min(df["NSSI_lifetime"]))
print(df["NSSI_lifetime"].value_counts(ascending=True))


print(max(df))

df["WIN_NSSI_lifetime"] = df["NSSI_lifetime"]

print(df[["NSSI_lifetime", "WIN_NSSI_lifetime"]].head())

df["Winsorized_NSSI"] = winsorize(df["WIN_NSSI_lifetime"],(0.05,0.05))

print(df[["NSSI_lifetime", "Winsorized_NSSI"]].head()
