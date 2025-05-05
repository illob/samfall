import pandas as pd
import re
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import operator
import os.path
save_path = ""

colnames = ["ord", "audk", "ordfl", "hluti","eink_ords","malsn_ords",
"malfr","mv","birt","beyg","mark","eink_beyg","malsn_beyg","gildi_beyg","auka"]

#colnames=["ord", "audk", "ordfl", "beyg", "mark"]
df = pd.read_csv("", names=colnames, delimiter=";")

#ordflokkar = ["ao", "fs", "nhm", "st", "uh", "lo", "afn", "rt", "fn", "to", "pfn", "gr", "kk", "kvk", "hk", "so"]
#orðflokkar til að sía út
ordflokkar = ["ao", "fs", "nhm", "st", "uh", "lo", "afn", "rt", 
"fn", "to", "pfn", "gr", "kk", "kvk", "hk"]


#henda út línum með orðflokkum sem við viljum ekki
df = df.drop(df[df['ordfl'].isin(ordflokkar)].index)

#vista nýtt csv með breytingum
df.to_csv(save_path + "", sep=";", index=False) 

#prenta einstök column gildi
for col in df:
    print(df[col].unique())
# Save the result back to a CSV file
#df.to_csv(save_path + "bin_nafnord.csv", sep=";", index=False)

