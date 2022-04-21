

# "conda install -c conda-forge pyreadstat"

import statistics as stat
import numpy as np
import pandas as pd
from scipy.stats.mstats import winsorize
import matplotlib.pyplot as plt
import pyreadstat

# leser inn datafil
df = pd.read_spss(r'C:\Users\alex_\Documents\Analysefil_BPD_Winsorizing.sav')

# Sjekker kolonner og NaN
print(df.columns)
print(df.isnull().sum())

# Her gjør vi en 90% winsorzing (derav "0.05,0.05" - 5% av her ende)
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


# Her visualiserer jeg dataen med boxplots
# Dette viser hvordan rangen av verdier blir skrenket inn mens majoriteten av tilfeller holder seg på samme sted (mao at vi strammer inn de ytterste 5%'ene)

plt.boxplot(df["NSSI_lifetime"])
plt.title('NSSI')
plt.show()

plt.boxplot(df["Win_NSSI_lifetime"])
plt.title('WIN_NSSI')
plt.show()

plt.boxplot(df["SA_livstid"])
plt.title('SA')
plt.show()

plt.boxplot(df["Win_SA_livstid"])
plt.title('WIN_SA')
plt.show()


# Linja under skriver ut det ferdige datasettet med de nye winsorizede variablene til den relevante mappa. Dette datasettet kan nå bli sendt til kunde
pyreadstat.write_sav(df, r'C:\Users\alex_\Documents\BPD_Win.sav')

# Her laster jeg datasettet inn igjen bare for å være helt sikker på at det har alt det skal ha
Win_check = pd.read_spss(r'C:\Users\alex_\Documents\BPD_Win.sav')
print(Win_check.columns)

# Her gjør jeg en kjapp øyesjekk
print(Win_check[["NSSI_lifetime", "Win_NSSI_lifetime"]].head(10))
print(Win_check[["SA_livstid", "Win_SA_livstid"]].head(10))





