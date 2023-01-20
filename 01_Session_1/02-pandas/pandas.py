import pandas as pd

# 1.0 DataFrame and Series Definition

# 2.0 DataFrame Creation
"""
dict = {
        "name":["Pedro","Antonio","Ángela","María"],
        "edad": [18,54,25,42],
        "email": ["pedro@gmail.com","antonio@hotmail.com","angela@yahoo.com","maria@icloud.com"]}

print(dict)

df = pd.DataFrame(dict)

print(df)

"""

# 3.0 Read table from csv or excel

df = pd.read_csv("dataframe.csv")
"""
print(df)
"""

# informacion general info()

# 4.0 Extract headers

headers = df.columns.to_list()

#print(headers)

# change headers names

# 5.0 Accessing elements

# 5.1 By columns

print(df[["name","email"]])

# by rows and labels: loc[]

print(df.loc[1, "name"])
print(df.loc[1, ["name","email"]])

#by rows and positions: iloc[]

print(df.iloc[1, 0])
# order the dataframe
# filters

# drop and append


#groupby()

#value_counts()

#info()

# write to csv or excel






