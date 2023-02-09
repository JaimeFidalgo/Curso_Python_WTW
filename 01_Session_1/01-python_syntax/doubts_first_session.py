
"""

#FIRST DOUBT

f = open("doubts_first_session.txt")

leer = f.readlines()

print(leer)

leer_new = []
for i in leer:
    if ("\n" in i):
        leer_new.append(i.replace("\n",""))
        
print(leer_new)

f.close()

"""
"""
#SECOND DOUBT
import pandas as pd

dict = {
        "name": "Jaime",
        "age": 28,
        "studies": ["engineer","professor"]}

print(dict)

df = pd.DataFrame(dict)

print(df)

new_studies = dict["studies"][0]

for i in range(1,len(dict["studies"]),1):
    new_studies += "/" + dict["studies"][i]
    
print(new_studies)    

dict["studies"] = [new_studies]

print(dict)

pd.DataFrame(dict)

"""