

# "conda install -c conda-forge pyreadstat"

import statistics as stat
import numpy as np
import pandas as pd
from scipy.stats.mstats import winsorize
import matplotlib.pyplot as plt
import pyreadstat

df = pd.read_spss(r'C:\Users\alex_\Documents\Anne Trana\Analysefil_BPD_Winsorizing.sav')

print(df.columns)
#print(df.isnull().sum())

# Winsorizing
df["Win_NSSI_lifetime"] = winsorize(df["NSSI_lifetime"],(0.05,0.05))
df["Win_SA_livstid"] = winsorize(df["SA_livstid"],(0.05,0.05))

# Kjapp test på resultater
print(df[["NSSI_lifetime", "Win_NSSI_lifetime"]].head(10))
print(df[["SA_livstid", "Win_SA_livstid"]].head(10))

# Sjekk for å se om gjennomsnittet forandrer seg veldig. Det skal det helst ikke gjøre for mye
print("NSSI gjennomsnitt før Win")
print(stat.mean(df["NSSI_lifetime"]))
print("NSSI gjennomsnitt etter Win")
print(stat.mean(df["Win_NSSI_lifetime"]))
print("SA gjennomsnitt før Win")
print(stat.mean(df["SA_livstid"]))
print("SA gjennomsnitt etter Win")
print(stat.mean(df["Win_SA_livstid"]))



plt.boxplot(df["NSSI_lifetime"])
plt.title('NSSI_lifetime')
plt.show()

plt.boxplot(df["Win_NSSI_lifetime"])
plt.title('Array with Outliers')
plt.show()

plt.boxplot(df["SA_livstid"])
plt.title('Array with Outliers')
plt.show()

plt.boxplot(df["Win_SA_livstid"])
plt.title('Array with Outliers')
plt.show()


Win = df[["Win_NSSI_lifetime", "Win_SA_livstid"]]

pyreadstat.write_sav(df, r'C:\Users\alex_\Documents\Anne Trana\BPD_Win.sav')

Win_check = pd.read_spss(r'C:\Users\alex_\Documents\Anne Trana\BPD_Win.sav')
print(Win_check.columns)

print(Win_check[["NSSI_lifetime", "Win_NSSI_lifetime"]].head(10))
print(Win_check[["SA_livstid", "Win_SA_livstid"]].head(10))





