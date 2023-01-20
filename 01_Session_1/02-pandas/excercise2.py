import pandas as pd

df = pd.read_csv("Liab_Trad_NB.csv")

print(df)

dims = df.shape

print(dims[0],dims[1])

df["year-month"] = str(df["val_year"]) + "/" + str(df["val_mth"])

print(df["year-month"])